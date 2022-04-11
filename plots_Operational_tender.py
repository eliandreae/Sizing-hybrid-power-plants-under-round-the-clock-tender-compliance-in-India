import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# Energy production by source
data1 = pd.read_csv('Sensitivity/Tender_bid/Operational_tender_hourly_HPC_250.csv')
data2 = pd.read_csv('Sensitivity/Tender_bid/Operational_tender_hourly_HPC_500.csv')
data3 = pd.read_csv('Sensitivity/Tender_bid/Operational_tender_hourly_HPC_750.csv')
data4 = pd.read_csv('Sensitivity/Tender_bid/Operational_tender_hourly_HPC_1000.csv')
x = ['250MW', '500MW', '750MW', '1000MW']
y1 = np.array([sum(data1['solar']), sum(data2['solar']), sum(data3['solar']), sum(data4['solar'])])
y2 = np.array([sum(data1['wind']), sum(data2['wind']), sum(data3['wind']), sum(data4['wind'])])
y3 = np.array([sum(data1['coal']), sum(data2['coal']), sum(data3['coal']), sum(data4['coal'])])
y4 = np.array([sum(data1['battery']), sum(data2['battery']), sum(data3['battery']), sum(data4['battery'])])

# plot bars in stack manner
plt.bar(x, y1, color='orangered')
plt.bar(x, y2, bottom=y1, color='dodgerblue')
plt.bar(x, y3, bottom=y1 + y2, color='darkgrey')
plt.bar(x, y4, bottom=y1 + y2 + y3, color='seagreen')
plt.xlabel("Bid size")
plt.ylabel("Energy [MWh]")
plt.legend(['Solar', 'Wind', 'Coal', 'Battery'])
plt.show()

# Non-delivered
data5 = pd.read_csv('Sensitivity/Tender_bid/Operational_tender_yearly_HPC_250.csv')
data6 = pd.read_csv('Sensitivity/Tender_bid/Operational_tender_yearly_HPC_500.csv')
data7 = pd.read_csv('Sensitivity/Tender_bid/Operational_tender_yearly_HPC_750.csv')
data8 = pd.read_csv('Sensitivity/Tender_bid/Operational_tender_yearly_HPC_1000.csv')
x = ['250MW', '500MW', '750MW', '1000MW']
y1 = np.array([sum(data5['nonDel_yearly']), sum(data6['nonDel_yearly']), sum(data7['nonDel_yearly']),
               sum(data8['nonDel_yearly'])])

# plot bars in stack manner
plt.bar(x, y1, color='steelblue')
plt.xlabel("Bid size")
plt.ylabel("Energy [MWh]")
plt.show()
