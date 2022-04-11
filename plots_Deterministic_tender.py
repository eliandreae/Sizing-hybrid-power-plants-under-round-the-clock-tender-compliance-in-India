import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data1 = pd.read_csv('Sensitivity/Tender_bid/Deterministic_tender_hourly_250.csv')
data2 = pd.read_csv('Sensitivity/Tender_bid/Deterministic_tender_hourly_500.csv')
data3 = pd.read_csv('Sensitivity/Tender_bid/Deterministic_tender_hourly_750.csv')
data4 = pd.read_csv('Sensitivity/Tender_bid/Deterministic_tender_hourly_1000.csv')
data5 = pd.read_csv('Sensitivity/Tender_bid/Deterministic_tender_overall.csv')
s1 = data5['250'].loc[0]
s2 = data5['500'].loc[0]
s3 = data5['750'].loc[0]
s4 = data5['1000'].loc[0]
w1 = data5['250'].loc[1]
w2 = data5['500'].loc[1]
w3 = data5['750'].loc[1]
w4 = data5['1000'].loc[1]
c1 = data5['250'].loc[2]
c2 = data5['500'].loc[2]
c3 = data5['750'].loc[2]
c4 = data5['1000'].loc[2]
b1 = data5['250'].loc[3]
b2 = data5['500'].loc[3]
b3 = data5['750'].loc[3]
b4 = data5['1000'].loc[3]
e1 = data5['250'].loc[4]
e2 = data5['500'].loc[4]
e3 = data5['750'].loc[4]
e4 = data5['1000'].loc[4]

N = 4
ind = np.arange(N)  # the x locations for the groups
width = 0.2       # the width of the bars
fig = plt.figure()
ax = fig.add_subplot(111)

svals = [s1, s2, s3, s4]
rects1 = ax.bar(ind, svals, width, color='tab:red')
wvals = [w1, w2, w3, w4]
rects2 = ax.bar(ind+width, wvals, width, color='mediumblue')
cvals = [c1, c2, c3, c4]
rects3 = ax.bar(ind+width*2, cvals, width, color='darkslategrey')
bvals = [b1, b2, b3, b4]
rects4 = ax.bar(ind+width*3, bvals, width, color='green')
evals = [e1, e2, e3, e4]
rects5 = ax.bar(ind+width*4, evals, width, color='lime')

ax.set_ylabel('Installed capacities')
ax.set_xlabel('Tender size')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('250MW', '500MW', '750MW', '1000MW') )
ax.legend( (rects1[0], rects2[0], rects3[0], rects4[0], rects5[0]), ('solar MW', 'wind MW', 'coal MW',
                                                                     'battery power MW', 'battery energy MWh') )
def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
                ha='center', va='bottom')
autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
plt.show()

# Energy production by source
x = ['250MW', '500MW', '750MW', '1000MW']
y1 = np.array([sum(data1['solar']), sum(data2['solar']), sum(data3['solar']), sum(data4['solar'])])
y2 = np.array([sum(data1['wind']), sum(data2['wind']), sum(data3['wind']), sum(data4['wind'])])
y3 = np.array([sum(data1['coal']), sum(data2['coal']), sum(data3['coal']), sum(data4['coal'])])
y4 = np.array([sum(data1['battery']), sum(data2['battery']), sum(data3['battery']), sum(data4['battery'])])

# plot bars in stack manner
plt.bar(x, y1, color='tab:red')
plt.bar(x, y2, bottom=y1, color='mediumblue')
plt.bar(x, y3, bottom=y1 + y2, color='darkslategrey')
plt.bar(x, y4, bottom=y1 + y2 + y3, color='green')
plt.xlabel("Tender size")
plt.ylabel("Energy [MWh]")
plt.legend(['solar', 'wind', 'coal', 'battery'])
plt.show()