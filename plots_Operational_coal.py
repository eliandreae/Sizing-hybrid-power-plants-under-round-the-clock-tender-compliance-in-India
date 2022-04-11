import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# Energy production by source
data1 = pd.read_csv('Sensitivity/Capacity_max/Operational_coal_max_hourly_HPC_0.csv')
data2 = pd.read_csv('Sensitivity/Capacity_max/Operational_coal_max_hourly_HPC_50.csv')
data3 = pd.read_csv('Sensitivity/Capacity_max/Operational_coal_max_hourly_HPC_100.csv')
data4 = pd.read_csv('Sensitivity/Capacity_max/Operational_coal_max_hourly_HPC_150.csv')
data5 = pd.read_csv('Sensitivity/Capacity_max/Operational_coal_max_hourly_HPC_200.csv')
data6 = pd.read_csv('Sensitivity/Capacity_max/Operational_coal_max_hourly_HPC_250.csv')
data61 = pd.read_csv('Sensitivity/Capacity_max/Operational_coal_max_hourly_HPC_300.csv')
x = ['0MW', '50MW', '100MW', '150MW', '200MW', '250MW', '300MW']
y1 = np.array([sum(data1['solar']), sum(data2['solar']), sum(data3['solar']), sum(data4['solar']),
               sum(data5['solar']), sum(data6['solar']), sum(data61['solar'])])
y2 = np.array([sum(data1['wind']), sum(data2['wind']), sum(data3['wind']), sum(data4['wind']),
               sum(data5['wind']), sum(data6['wind']), sum(data61['wind'])])
y3 = np.array([sum(data1['coal']), sum(data2['coal']), sum(data3['coal']), sum(data4['coal']),
               sum(data5['coal']), sum(data6['coal']), sum(data61['coal'])])
y4 = np.array([sum(data1['battery']), sum(data2['battery']), sum(data3['battery']), sum(data4['battery']),
               sum(data5['battery']), sum(data6['battery']), sum(data61['battery'])])

# plot bars in stack manner
plt.bar(x, y1, color='orangered')
plt.bar(x, y2, bottom=y1, color='dodgerblue')
plt.bar(x, y3, bottom=y1 + y2, color='darkgrey')
plt.bar(x, y4, bottom=y1 + y2 + y3, color='seagreen')
plt.xlabel("Coal capacity")
plt.ylabel("Energy [MWh]")
plt.legend(['Solar', 'Wind', 'Coal', 'Battery'])
plt.show()

# Non-delivered
data7 = pd.read_csv('Sensitivity/Capacity_max/Operational_coal_max_yearly_HPC_0.csv')
data8 = pd.read_csv('Sensitivity/Capacity_max/Operational_coal_max_yearly_HPC_50.csv')
data9 = pd.read_csv('Sensitivity/Capacity_max/Operational_coal_max_yearly_HPC_100.csv')
data10 = pd.read_csv('Sensitivity/Capacity_max/Operational_coal_max_yearly_HPC_150.csv')
data11 = pd.read_csv('Sensitivity/Capacity_max/Operational_coal_max_yearly_HPC_200.csv')
data12 = pd.read_csv('Sensitivity/Capacity_max/Operational_coal_max_yearly_HPC_250.csv')
data13 = pd.read_csv('Sensitivity/Capacity_max/Operational_coal_max_yearly_HPC_300.csv')
x = ['0MW', '50MW', '100MW', '150MW', '200MW', '250MW', '300MW']
y1 = np.array([sum(data7['nonDel_yearly']), sum(data8['nonDel_yearly']), sum(data9['nonDel_yearly']),
               sum(data10['nonDel_yearly']), sum(data11['nonDel_yearly']), sum(data12['nonDel_yearly']),
               sum(data13['nonDel_yearly'])])

# plot bars in stack manner
plt.bar(x, y1, color='steelblue')
plt.xlabel("Coal capacity")
plt.ylabel("Energy [MWh]")
plt.show()


x = ['solar', 'wind', 'coal']
y1 = np.array([60])
y2 = np.array([345])
y3 = np.array([206])
# plot bars in stack manner
plt.bar(x, y1, color='orangered')
plt.bar(x, y2, color='dodgerblue')
plt.bar(x, y3, color='darkgrey')
plt.ylabel("Installed capacity [MW]")
plt.show()