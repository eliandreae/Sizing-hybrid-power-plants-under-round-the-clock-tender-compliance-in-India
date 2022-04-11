import matplotlib.pyplot as plt
import pandas as pd
dataInv = pd.read_csv('Results/Results_Investment_hourly.csv')
dataInvY = pd.read_csv('Results/Results_Investment_yearly.csv')
dataDet = pd.read_csv('Results/Results_Deterministic_hourly.csv')
dataDetY = pd.read_csv('Results/Results_Deterministic_yearly.csv')

# Tender + total production
fig, ax = plt.subplots()
ax.plot(dataInv['tender'], label='Power requirement', linestyle='solid', color='firebrick')
ax.plot(dataInv['total production'], label='Total production', linestyle='dashed', color='limegreen')
ax.plot(dataDet['tender'], label='Power requirement compl.', linestyle='solid', color='darkmagenta')
ax.plot(dataDet['total production'], label='Total production compl.', linestyle='dashed', color='deepskyblue')
ax.set_xlabel('Time [hour]')
ax.set_ylabel('Production [MWh/h]')
ax.legend(loc='best')
ax.set_xlim((0, 72))
plt.show()

# Emissions 
fig, ax = plt.subplots()
ax = dataInvY['CO2'].plot.bar(x='Time [years]', y='without compliance', label='Emissions without compliance', rot=0,
                              color='lightslategrey')
ax = dataDetY['CO2'].plot.bar(x='Time [years]', y='with compliance', label='Emissions with compliance', rot=0,
                              color='darkturquoise')
ax.set_xlabel('Time [year]')
ax.set_ylabel('Tonnes of CO2')
ax.legend(loc='best')
plt.show()

# Revenues
fig, ax = plt.subplots()
ax = dataInvY['Revenue'].plot.bar(label='Revenues without compliance', rot=0, color='mediumblue')
ax = dataDetY['Revenue'].plot.bar(label='Revenues with compliance', rot=0, color='lime')
ax.set_xlabel('Time [year]')
ax.set_ylabel('MWh')
ax.legend(loc='best')
plt.show()



