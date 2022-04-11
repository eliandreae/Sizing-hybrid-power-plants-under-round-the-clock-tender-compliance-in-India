import matplotlib.pyplot as plt
import pandas as pd
Nyears = 1
from parameters_NEW import Parameters
CFsolar, CFwind, prices, tau, PPA, penalty_utilization_yearly, penalty_renewable,\
           Cmin, eta_round, SoCmin, SoCmax, cycles, deg_per_hour, coalCO2Emis, eta_fuel, solarC, windC, coalFuelC, \
           chargeC, solarOpexVar, windOpexVar, coalOpexVar, coalEmisC, batteryOpexVar, solarOpexFix, windOpexFix, \
           coalOpexFix, batteryOpexFix, EOpexFix, solarCapex, windCapex, coalCapex, batteryCapex, BOS, ECapex, GC, r, \
           util_yearly, renew_share, PPA_dyn, penalty_utilization_yearly_dyn, penalty_renewable_dyn, \
           opex_refurbish_bat, opex_refurbish_E, init = Parameters(Nyears)
data = pd.read_csv('Results_HPC/Results_Operational_hourly_HPC.csv')

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

# Battery power + charge + discharge vs. energy
fig, ax = plt.subplots()
ax.plot(data['battery'], label='Battery', linestyle='solid', color='seagreen')
ax.plot(data['discharge'], label='Discharge', linestyle='dotted', color='darkviolet')
ax.plot(data['charge'], label='Charge', linestyle='dotted', color='orange')
ax.plot(data['SoC'], label='SoC', linestyle='dotted', color='lime')
ax.set_xlabel('Time [hour]')
ax.set_ylabel('Production [MWh/h]')
ax.legend(loc='best')
ax.set_xlim((0, 72))
plt.show()

# Total production vs. market price with power requirement
fig, ax = plt.subplots()
lns1 = ax.plot(data['total production'], label='Total production', color='limegreen')
lns3 = ax.plot(data['tender'], label='Power requirement', linestyle='solid', color='firebrick')
ax.set_xlabel('Time [hour]')
ax.set_ylabel('Production [MWh/h]')
ax2 = ax.twinx()
lns2 = ax2.plot(prices, label='Market price', color='blue')
ax2.set_ylabel('Market price [€/MWh]')
lns = lns1+lns3+lns2
labs = [l.get_label() for l in lns]
ax.legend(lns, labs, loc='best')
ax.set_xlim((0, 72))
plt.show()















