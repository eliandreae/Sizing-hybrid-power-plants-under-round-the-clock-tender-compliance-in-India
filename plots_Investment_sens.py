import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
list1 = [250]*9000
list2 = [500]*9000
list3 = [750]*9000
list4 = [1000]*9000

# Tender + total production
data1 = pd.read_csv('Sensitivity/Tender_bid/Investment_tender_hourly_250.csv')
data2 = pd.read_csv('Sensitivity/Tender_bid/Investment_tender_hourly_500.csv')
data3 = pd.read_csv('Sensitivity/Tender_bid/Investment_tender_hourly_750.csv')
data4 = pd.read_csv('Sensitivity/Tender_bid/Investment_tender_hourly_1000.csv')

fig, ax = plt.subplots()
ax.plot(data1['total production'], label='production for 250MW tender', linestyle='solid', color='mediumblue')
ax.plot(list1, linestyle='dashed', color='black')
ax.plot(data2['total production'], label='production for 500MW tender', linestyle='solid', color='green')
ax.plot(list2, linestyle='dashed', color='black')
ax.plot(data3['total production'], label='production for 750MW tender', linestyle='solid', color='darkslategrey')
ax.plot(list3, linestyle='dashed', color='black')
ax.plot(data4['total production'], label='production for 1000MW tender', linestyle='solid', color='orange')
ax.plot(list4, linestyle='dashed', color='black')
ax.set_xlabel('Time [hour]')
ax.set_ylabel('Production [MWh]')
ax.legend(loc='upper right')
ax.set_xlim((0, 72))
plt.show()

# Capacities
data5 = pd.read_csv('Sensitivity/Tender_bid/Investment_tender_overall.csv')
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
rects1 = ax.bar(ind, svals, width, color='orangered')
wvals = [w1, w2, w3, w4]
rects2 = ax.bar(ind+width, wvals, width, color='dodgerblue')
cvals = [c1, c2, c3, c4]
rects3 = ax.bar(ind+width*2, cvals, width, color='darkgrey')
bvals = [b1, b2, b3, b4]
rects4 = ax.bar(ind+width*3, bvals, width, color='seagreen')
evals = [e1, e2, e3, e4]
rects5 = ax.bar(ind+width*4, evals, width, color='lime')

ax.set_ylabel('Installed capacities')
ax.set_xlabel('Power requirement')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('250MW', '500MW', '750MW', '1000MW') )
ax.legend( (rects1[0], rects2[0], rects3[0], rects4[0], rects5[0]), ('Solar MW', 'Wind MW', 'Coal MW',
                                                                     'Battery power MW', 'Battery energy MWh') )
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
plt.bar(x, y1, color='orangered')
plt.bar(x, y2, bottom=y1, color='dodgerblue')
plt.bar(x, y3, bottom=y1 + y2, color='darkgrey')
plt.bar(x, y4, bottom=y1 + y2 + y3, color='seagreen')
plt.xlabel("Power requirement")
plt.ylabel("Energy [MWh]")
plt.legend(['Solar', 'Wind', 'Coal', 'Battery'])
plt.show()




# Battery cost scale
data10 = pd.read_csv('Sensitivity/Battery_cost/Investment_batScale_hourly_0.25.csv')
data11 = pd.read_csv('Sensitivity/Battery_cost/Investment_batScale_hourly_0.5.csv')
data12 = pd.read_csv('Sensitivity/Battery_cost/Investment_batScale_hourly_0.75.csv')
data13 = pd.read_csv('Sensitivity/Battery_cost/Investment_batScale_hourly_0.9.csv')
data14 = pd.read_csv('Sensitivity/Battery_cost/Investment_batScale_hourly_1.csv')

fig, ax = plt.subplots()
ax.plot(data10['total production'], label='Production for 250MW tender', linestyle='solid', color='mediumblue')
ax.plot(list1, linestyle='dashed', color='black')
ax.plot(data11['total production'], label='Production for 500MW tender', linestyle='solid', color='green')
ax.plot(data12['total production'], label='Production for 750MW tender', linestyle='solid', color='darkslategrey')
ax.plot(data13['total production'], label='Production for 1000MW tender', linestyle='solid', color='orange')
ax.plot(data14['total production'], label='Production for 1000MW tender', linestyle='solid', color='orange')
ax.set_xlabel('Time [hour]')
ax.set_ylabel('Production [MWh]')
ax.legend(loc='upper right')
ax.set_xlim((0, 72))
plt.show()


# Revenue and cost distribution
data11 = pd.read_csv('Sensitivity/Battery_cost/Investment_batScale_yearly_0.25.csv')
data22 = pd.read_csv('Sensitivity/Battery_cost/Investment_batScale_yearly_0.5.csv')
data33 = pd.read_csv('Sensitivity/Battery_cost/Investment_batScale_yearly_0.75.csv')
data44 = pd.read_csv('Sensitivity/Battery_cost/Investment_batScale_yearly_0.9.csv')
data55 = pd.read_csv('Sensitivity/Battery_cost/Investment_batScale_yearly_1.csv')

p1 = data11['PPA revenue']
m1 = data11['market revenue']
c1 = (data11['OpexFix'])*(-1)
o1 = (data11['OpexVar'])*(-1)
f1 = (data11['ProdCost'])*(-1)
k1 = (data11['Penalty'])*(-1)

p2 = data22['PPA revenue']
m2 = data22['market revenue']
c2 = (data22['OpexFix'])*(-1)
o2 = (data22['OpexVar'])*(-1)
f2 = (data22['ProdCost'])*(-1)
k2 = (data22['Penalty'])*(-1)

p3 = data33['PPA revenue']
m3 = data33['market revenue']
c3 = (data33['OpexFix'])*(-1)
o3 = (data33['OpexVar'])*(-1)
f3 = (data33['ProdCost'])*(-1)
k3 = (data33['Penalty'])*(-1)

p4 = data44['PPA revenue']
m4 = data44['market revenue']
c4 = (data44['OpexFix'])*(-1)
o4 = (data44['OpexVar'])*(-1)
f4 = (data44['ProdCost'])*(-1)
k4 = (data44['Penalty'])*(-1)

p5 = data55['PPA revenue']
m5 = data55['market revenue']
c5 = (data55['OpexFix'])*(-1)
o5 = (data55['OpexVar'])*(-1)
f5 = (data55['ProdCost'])*(-1)
k5 = (data55['Penalty'])*(-1)

x = ['0.25', '0.5', '0.75', '0.9', '1.0']
y1 = np.array([sum(p1), sum(p2), sum(p3), sum(p4), sum(p5)])
y2 = np.array([sum(m1), sum(m2), sum(m3), sum(m4), sum(m5)])

# plot bars in stack manner
plt.bar(x, y1, color='limegreen')
plt.bar(x, y2, bottom=y1, color='springgreen')

x = ['0.25', '0.5', '0.75', '0.9', '1.0']
y3 = np.array([sum(c1), sum(c2), sum(c3), sum(c4), sum(c5)])
y4 = np.array([sum(o1), sum(o2), sum(o3), sum(o4), sum(o5)])
y5 = np.array([sum(f1), sum(f2), sum(f3), sum(f4), sum(f5)])
y6 = np.array([sum(k1), sum(k2), sum(k3), sum(k4), sum(k5)])

# plot bars in stack manner
plt.bar(x, y3, color='midnightblue')
plt.bar(x, y4, bottom=y3, color='aqua')
plt.bar(x, y5, bottom=y3 + y4, color='dimgrey')
plt.bar(x, y6, bottom=y3 + y4 + y5, color='red')
plt.xlabel("Battery cost adjustment")
plt.ylabel("Costs and revenues [€]")
plt.legend(['Revenue from PPA', 'Revenue from market', 'Fixed opex', 'Variable opex', 'Fuel cost', 'Penalty cost'])
plt.axhline(y=0, linewidth=1, color='black')
plt.show()

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

# Capacities
data15 = pd.read_csv('Sensitivity/Battery_cost/Investment_batScale_overall.csv')
s1 = data15['0.25'].loc[0]
s2 = data15['0.5'].loc[0]
s3 = data15['0.75'].loc[0]
s4 = data15['0.9'].loc[0]
s5 = data15['1.0'].loc[0]
w1 = data15['0.25'].loc[1]
w2 = data15['0.5'].loc[1]
w3 = data15['0.75'].loc[1]
w4 = data15['0.9'].loc[1]
w5 = data15['1.0'].loc[1]
c1 = data15['0.25'].loc[2]
c2 = data15['0.5'].loc[2]
c3 = data15['0.75'].loc[2]
c4 = data15['0.9'].loc[2]
c5 = data15['1.0'].loc[2]
b1 = data15['0.25'].loc[3]
b2 = data15['0.5'].loc[3]
b3 = data15['0.75'].loc[3]
b4 = data15['0.9'].loc[3]
b5 = data15['1.0'].loc[3]
e1 = data15['0.25'].loc[4]
e2 = data15['0.5'].loc[4]
e3 = data15['0.75'].loc[4]
e4 = data15['0.9'].loc[4]
e5 = data15['1.0'].loc[4]

N = 5
ind = np.arange(N)  # the x locations for the groups
width = 0.2       # the width of the bars
fig = plt.figure()
ax = fig.add_subplot(111)

svals = [s1, s2, s3, s4, s5]
rects1 = ax.bar(ind, svals, width, color='orangered')
wvals = [w1, w2, w3, w4, w5]
rects2 = ax.bar(ind+width, wvals, width, color='dodgerblue')
cvals = [c1, c2, c3, c4, c5]
rects3 = ax.bar(ind+width*2, cvals, width, color='darkgrey')
bvals = [b1, b2, b3, b4, b4]
rects4 = ax.bar(ind+width*3, bvals, width, color='seagreen')
evals = [e1, e2, e3, e4, e5]
rects5 = ax.bar(ind+width*4, evals, width, color='lime')

ax.set_ylabel('Installed capacities')
ax.set_xlabel('Battery cost adjustment')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('0.25', '0.5', '0.75', '0.9', '1.0') )
ax.legend( (rects1[0], rects2[0], rects3[0], rects4[0], rects5[0]), ('Solar MW', 'Wind MW', 'Coal MW',
                                                                     'Battery power MW', 'Battery energy MWh') )
def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
                ha='center', va='bottom')
autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)
autolabel(rects5)
plt.show()

# Battery power + charge + discharge vs. energy
fig, ax = plt.subplots()
ax.plot(data10['battery'], label='battery', linestyle='solid', color='green')
ax.plot(data10['discharge'], label='discharge', linestyle='dotted', color='mediumblue')
ax.plot(data10['charge'], label='charge', linestyle='dotted', color='orange')
ax.set_xlabel('Time [hour]')
ax.set_ylabel('Production [MWh/h]')
ax.legend(loc='best')
ax.set_xlim((0, 72))
plt.show()

# Duration curve
bat = pd.DataFrame(data10['discharge'])
bat = bat.sort_values('discharge')
bat = bat.reset_index(drop=True)

fig, ax = plt.subplots()
ax.plot(bat, label='battery production', linestyle='solid', color='darkviolet')
ax.set_ylabel('Production [MWh/h]')
ax.legend(loc='best')
plt.show()


bat = pd.DataFrame(data10['discharge'])
bat = bat.sort_values('discharge', ascending=False)
bat = bat.reset_index(drop=True)
exceedence = np.arange(1.,len(bat)+1) / len(bat)

plt.plot(exceedence*100, bat, color='darkviolet', label='Discharge duration for 25% battery cost')
plt.legend(loc='best')
plt.xlabel("Exceedence [%]")
plt.ylabel("Discharge [MWh]")
plt.show()

# Energy mix
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Solar', 'Wind', 'Coal', 'Battery power', 'Battery energy'
color = 'orangered', 'dodgerblue', 'darkgrey', 'seagreen', 'lime'
sizes = [(83/781*100), (429/781*100), (190/781*100), (25/781*100), (54/781*100)]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, colors=color, autopct='%1.1f%%')
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

labels = 'Solar', 'Wind', 'Coal'
color = 'orangered', 'dodgerblue', 'darkgrey'
sizes = [(60/781*100), (345/781*100), (206/781*100)]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, colors=color, autopct='%1.1f%%')
ax1.axis('equal')  
plt.show()






