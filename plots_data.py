import matplotlib.pyplot as plt
Nyears = 30
from clean_data_NEW import get_clean_data
all_data, Ts, Y, Yp, Years, Hours_in_year = get_clean_data(Nyears)
from parameters_NEW import Parameters
CFsolar, CFwind, prices, tau, PPA, penalty_utilization_yearly, penalty_renewable,\
           Cmin, eta_round, SoCmin, SoCmax, cycles, deg_per_hour, coalCO2Emis, eta_fuel, solarC, windC, coalFuelC, \
           chargeC, solarOpexVar, windOpexVar, coalOpexVar, coalEmisC, batteryOpexVar, solarOpexFix, windOpexFix, \
           coalOpexFix, batteryOpexFix, EOpexFix, solarCapex, windCapex, coalCapex, batteryCapex, BOS, ECapex, GC, r, \
           util_yearly, renew_share, PPA_dyn, penalty_utilization_yearly_dyn, penalty_renewable_dyn, \
           opex_refurbish_bat, opex_refurbish_E, init = Parameters(Nyears)

Wind = all_data['Wind']
PV = all_data['PV']
MarketPrices = all_data['2019 euro']
coalPrice = all_data['Coal price']

# Solar and wind power
fig, ax = plt.subplots()
ax.plot(all_data['Wind'], label='Wind', linestyle='solid', color='dodgerblue')
ax.plot(all_data['PV'], label='Solar', linestyle='solid', color='orangered')
ax.set_xlabel('Time [hour]')
ax.set_ylabel('Power [kW]')
ax.legend(loc='upper left')
ax.set_xlim((140, 280))
plt.show()

# Market and coal prices
fig, ax = plt.subplots()
ax.plot(all_data['2019 euro'], label='Market price', linestyle='solid', color='blue')
ax.plot(all_data['Coal price'], label='Coal price', linestyle='solid', color='darkslategrey')
ax.set_ylabel('Price [€/MWh]')
ax.legend(loc='upper left')
ax.set_xlim((0, 8760))
plt.show()

# Coal prices
fig, ax = plt.subplots()
ax.plot(all_data['Coal price'], label='Coal price', linestyle='solid', color='darkslategrey')
ax.set_ylabel('Price [€/MWh]')
ax.set_xlim((0, len(Ts)))
plt.show()

# Boxplot for capacity factors
data = [CFwind, CFsolar]
medianprops = dict(linestyle='-', linewidth=2, color='black')
box = plt.boxplot(data, patch_artist=True, labels=['Wind capacity factor', 'Solar capacity factor'],
                  medianprops=medianprops)
colors = ['lightskyblue', 'orange']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
plt.show()

# Wind
data = [CFwind[0:8760], CFwind[8760:17520]]
medianprops = dict(linestyle='-', linewidth=2, color='black')
box = plt.boxplot(data, patch_artist=True, labels=['2000', '2001'],
                  medianprops=medianprops)
colors = ['lightskyblue', 'orange']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
plt.show()

# Wind
data = [CFwind[0:730], CFwind[730:1460], CFwind[1460:2190], CFwind[2190:2920], CFwind[2920:3650], CFwind[3650:4380],
        CFwind[4380:5110], CFwind[5110:5840], CFwind[5840:6570], CFwind[6570:7300], CFwind[7300:8030], CFwind[8030:8760]]
medianprops = dict(linestyle='-', linewidth=2, color='black')
box = plt.boxplot(data, patch_artist=True, labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
                                                   'Nov', 'Dec'],
                  medianprops=medianprops)
colors = ['lightskyblue', 'lightskyblue', 'lightskyblue', 'lightskyblue', 'lightskyblue', 'lightskyblue',
          'lightskyblue', 'lightskyblue', 'lightskyblue', 'lightskyblue', 'lightskyblue', 'lightskyblue']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
plt.show()

# Solar
data = [CFsolar[0:730], CFsolar[730:1460], CFsolar[1460:2190], CFsolar[2190:2920], CFsolar[2920:3650],
        CFsolar[3650:4380], CFsolar[4380:5110], CFsolar[5110:5840], CFsolar[5840:6570], CFsolar[6570:7300],
        CFsolar[7300:8030], CFsolar[8030:8760]]
medianprops = dict(linestyle='-', linewidth=2, color='black')
box = plt.boxplot(data, patch_artist=True, labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
                                                   'Nov', 'Dec'],
                  medianprops=medianprops)
colors = ['orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange',
          'orange']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
plt.show()