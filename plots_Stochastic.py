import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# Revenue and cost distribution
data11 = pd.read_csv('Results_HPC/Results_Stochastic_yearly_HPC.csv')
data22 = pd.read_csv('Results_HPC/Results_Deterministic_yearly_HPC.csv')
data11 = data11.sort_values('scenario')
data11 = data11.reset_index(drop=True)
data11_1 = data11.loc[0:29]
data11_2 = data11.loc[30:59]

p1 = data22['PPA revenue']
m1 = data22['market revenue']
c1 = (data22['OpexFix'])*(-1)
o1 = (data22['OpexVar'])*(-1)
f1 = (data22['ProdCost'])*(-1)
k1 = (data22['Penalty'])*(-1)

p2 = data11_1['PPA revenue']
m2 = data11_1['market revenue']
c2 = (data11_1['OpexFix'])*(-1)
o2 = (data11_1['OpexVar'])*(-1)
f2 = (data11_1['ProdCost'])*(-1)
k2 = (data11_1['Penalty'])*(-1)

p3 = data11_2['PPA revenue']
m3 = data11_2['market revenue']
c3 = (data11_2['OpexFix'])*(-1)
o3 = (data11_2['OpexVar'])*(-1)
f3 = (data11_2['ProdCost'])*(-1)
k3 = (data11_2['Penalty'])*(-1)

x = ['Deterministic', 'Scenario 1', 'Scenario 2']
y1 = np.array([sum(p1), sum(p2), sum(p3)])
y2 = np.array([sum(m1), sum(m2), sum(m3)])

# plot bars in stack manner
plt.bar(x, y1, color='limegreen')
plt.bar(x, y2, bottom=y1, color='springgreen')

x = ['Deterministic', 'Scenario 1', 'Scenario 2']
y3 = np.array([sum(c1), sum(c2), sum(c3)])
y4 = np.array([sum(o1), sum(o2), sum(o3)])
y5 = np.array([sum(f1), sum(f2), sum(f3)])
y6 = np.array([sum(k1), sum(k2), sum(k3)])

# plot bars in stack manner
plt.bar(x, y3, color='midnightblue')
plt.bar(x, y4, bottom=y3, color='aqua')
plt.bar(x, y5, bottom=y3 + y4, color='dimgrey')
plt.bar(x, y6, bottom=y3 + y4 + y5, color='red')
plt.ylabel("Costs and revenues [€]")
plt.legend(['Revenue from PPA', 'Revenue from market', 'Fixed opex', 'Variable opex', 'Fuel cost', 'Penalty cost'])
plt.show()

# Emissions
x = ['Deterministic', 'Scenario 1', 'Scenario 2']
y1 = np.array([sum(data22['CO2']), sum(data11_1['CO2']), sum(data11_2['CO2'])])

# plot bars in stack manner
plt.bar(x, y1, color='lightslategrey')
plt.ylabel("Tonnes of CO2")
plt.legend(['CO2 emissions'])
plt.show()

# Energy production by source
data1 = pd.read_csv('Results_HPC/Results_Stochastic_scen3_hourly_HPC.csv')
data2 = pd.read_csv('Results_HPC/Results_Deterministic_hourly_HPC.csv')
data1 = data1.sort_values('scenario')
data1 = data1.reset_index(drop=True)
data1_1 = data1.loc[0:262799]
data1_2 = data1.loc[262800:525599]

x = ['Deterministic', 'Scenario 1', 'Scenario 2']
y1 = np.array([sum(data2['solar']), sum(data1_1['solar']), sum(data1_2['solar'])])
y2 = np.array([sum(data2['wind']), sum(data1_1['wind']), sum(data1_2['wind'])])
y3 = np.array([sum(data2['coal']), sum(data1_1['coal']), sum(data1_2['coal'])])
y4 = np.array([sum(data2['battery']), sum(data1_1['battery']), sum(data1_2['battery'])])

# plot bars in stack manner
plt.bar(x, y1, color='orangered')
plt.bar(x, y2, bottom=y1, color='dodgerblue')
plt.bar(x, y3, bottom=y1 + y2, color='darkgrey')
plt.bar(x, y4, bottom=y1 + y2 + y3, color='seagreen')
plt.ylabel("Energy [MWh]")
plt.legend(['Solar', 'Wind', 'Coal', 'Battery'])
plt.show()
