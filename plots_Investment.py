import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('Results_HPC/Results_Investment_hourly_HPC.csv')
dataY = pd.read_csv('Results_HPC/Results_Investment_yearly_HPC.csv')

# Production
fig, ax = plt.subplots()
ax.plot(data['solar'], label='Solar', linestyle='solid', color='orangered')
ax.plot(data['wind'], label='Wind', linestyle='solid', color='dodgerblue')
ax.plot(data['coal'], label='Coal', linestyle='solid', color='darkgrey')
ax.plot(data['battery'], label='Battery', linestyle='dashed', color='seagreen')
ax.plot(data['SoC'], label='SoC', linestyle='dotted', color='lime')
ax.set_xlabel('Time [hour]')
ax.set_ylabel('Production [MWh/h]')
ax.legend(loc='best')
ax.set_xlim((0, 72))
plt.show()

# Tender + total production
fig, ax = plt.subplots()
ax.plot(data['tender'], label='Power requirement', linestyle='solid', color='firebrick')
ax.plot(data['total production'], label='Total production', linestyle='dashed', color='limegreen')
ax.set_xlabel('Time [hour]')
ax.set_ylabel('Production [MWh/h]')
ax.legend(loc='best')
ax.set_xlim((0, 72))
plt.show()

# Revenue and cost distribution
fig, ax = plt.subplots()
t = range(1, 31)
p = dataY['PPA revenue']
m = dataY['market revenue']
c = (dataY['OpexFix'])*(-1)
o = (dataY['OpexVar'])*(-1)
f = (dataY['ProdCost'])*(-1)
k = (dataY['Penalty'])*(-1)
plt.stackplot(t, c, o, f, k, labels=['Fixed opex', 'Variable opex', 'Fuel cost', 'Penalty cost'],
              colors=['midnightblue', 'aqua', 'dimgrey', 'red'])
plt.stackplot(t, m, p, labels=['Revenue from market', 'Revenue from PPA'],
              colors=['springgreen', 'limegreen'])
plt.ylabel('Costs and revenues [€]')
plt.xlabel('Time [year]')
plt.legend(loc='best', ncol=3)
plt.axhline(y=0, linewidth=1, color='black')
plt.show()

# Non-delivered
fig, ax = plt.subplots()
d = dataY['nonDel_yearly']
ax = d.loc[0:24].plot.bar(label='Power availability shortfall', rot=0, color='steelblue')
ax.set_xlabel('Time [year]')
ax.set_ylabel('Shortfall [MWh]')
plt.show()