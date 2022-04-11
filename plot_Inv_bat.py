import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data11 = pd.read_csv('Sensitivity/Battery_cost/Investment_batScale_yearly_0.25.csv')
data1 = pd.read_csv('Sensitivity/Battery_cost/Investment_batScale_hourly_0.25.csv')
data15 = pd.read_csv('Sensitivity/Battery_cost/Investment_batScale_overall.csv')

# Energy production by source
data1 = pd.read_csv('Sensitivity/Battery_cost/Investment_batScale_hourly_0.25.csv')
data2 = pd.read_csv('Sensitivity/Battery_cost/Investment_batScale_hourly_0.5.csv')
data3 = pd.read_csv('Sensitivity/Battery_cost/Investment_batScale_hourly_0.75.csv')
data4 = pd.read_csv('Sensitivity/Battery_cost/Investment_batScale_hourly_0.9.csv')
data5 = pd.read_csv('Sensitivity/Battery_cost/Investment_batScale_hourly_1.csv')

x = ['0.25', '0.5', '0.75', '0.9', '1.0']
y1 = np.array([sum(data1['solar']), sum(data2['solar']), sum(data3['solar']), sum(data4['solar']),
               sum(data5['solar'])])
y2 = np.array([sum(data1['wind']), sum(data2['wind']), sum(data3['wind']), sum(data4['wind']),
               sum(data5['wind'])])
y3 = np.array([sum(data1['coal']), sum(data2['coal']), sum(data3['coal']), sum(data4['coal']),
               sum(data5['coal'])])
y4 = np.array([sum(data1['battery']), sum(data2['battery']), sum(data3['battery']), sum(data4['battery']),
               sum(data5['battery'])])

# plot bars in stack manner
plt.bar(x, y1, color='orangered')
plt.bar(x, y2, bottom=y1, color='dodgerblue')
plt.bar(x, y3, bottom=y1 + y2, color='darkgrey')
plt.bar(x, y4, bottom=y1 + y2 + y3, color='seagreen')
plt.xlabel("Battery cost adjustment")
plt.ylabel("Energy [MWh]")
plt.legend(['Solar', 'Wind', 'Coal', 'Battery'])
plt.show()

# Energy
x = ['Battery', 'Solar', 'Wind', 'Coal']
y1 = np.array([sum(data1['battery'])])
y2 = np.array([sum(data1['solar'])])
y3 = np.array([sum(data1['wind'])])
y4 = np.array([sum(data1['coal'])])

plt.bar(x, y1, color='seagreen')
plt.bar(x, y2, color='orangered')
plt.bar(x, y3, color='dodgerblue')
plt.bar(x, y4, color='darkgrey')
plt.xlabel("Adjusted battery cost at 0,25 of original")
plt.ylabel("Energy [MWh]")
plt.legend(['Battery', 'Solar', 'Wind', 'Coal'])
plt.show()



# Energy for 0.25
s1 = sum(data1['battery'])
w1 = sum(data1['solar'])
c1 = sum(data1['wind'])
b1 = sum(data1['coal'])

N = 1
ind = np.arange(N)  # the x locations for the groups
width = 0.2       # the width of the bars
fig = plt.figure()
ax = fig.add_subplot(111)

svals = [s1]
rects1 = ax.bar(ind, svals, width, color='seagreen')
wvals = [w1]
rects2 = ax.bar(ind+width, wvals, width, color='orangered')
cvals = [c1]
rects3 = ax.bar(ind+width*2, cvals, width, color='dodgerblue')
bvals = [b1]
rects4 = ax.bar(ind+width*3, bvals, width, color='darkgrey')

ax.set_ylabel('Energy [MWh]')
ax.set_xlabel('Adjusted battery cost at 0,25 of original')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('Battery', 'Solar', 'Wind', 'Coal') )
ax.legend( (rects1[0], rects2[0], rects3[0], rects4[0]), ('Battery', 'Solar', 'Wind', 'Coal') )
def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
                ha='center', va='bottom')

plt.show()



