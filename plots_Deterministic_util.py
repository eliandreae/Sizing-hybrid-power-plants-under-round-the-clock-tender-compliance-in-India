import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
data5 = pd.read_csv('Sensitivity/Util_yearly/Deterministic_util_yearly_overall.csv')
s1 = data5['0.7'].loc[0]
s2 = data5['0.75'].loc[0]
s3 = data5['0.8'].loc[0]
s4 = data5['0.85'].loc[0]
s5 = data5['0.9'].loc[0]
s6 = data5['0.95'].loc[0]
s7 = data5['1.0'].loc[0]

w1 = data5['0.7'].loc[1]
w2 = data5['0.75'].loc[1]
w3 = data5['0.8'].loc[1]
w4 = data5['0.85'].loc[1]
w5 = data5['0.9'].loc[1]
w6 = data5['0.95'].loc[1]
w7 = data5['1.0'].loc[1]

c1 = data5['0.7'].loc[2]
c2 = data5['0.75'].loc[2]
c3 = data5['0.8'].loc[2]
c4 = data5['0.85'].loc[2]
c5 = data5['0.9'].loc[2]
c6 = data5['0.95'].loc[2]
c7 = data5['1.0'].loc[2]

b1 = data5['0.7'].loc[3]
b2 = data5['0.75'].loc[3]
b3 = data5['0.8'].loc[3]
b4 = data5['0.85'].loc[3]
b5 = data5['0.9'].loc[3]
b6 = data5['0.95'].loc[3]
b7 = data5['1.0'].loc[3]

e1 = data5['0.7'].loc[4]
e2 = data5['0.75'].loc[4]
e3 = data5['0.8'].loc[4]
e4 = data5['0.85'].loc[4]
e5 = data5['0.9'].loc[4]
e6 = data5['0.95'].loc[4]
e7 = data5['1.0'].loc[4]

N = 7
ind = np.arange(N)  # the x locations for the groups
width = 0.15       # the width of the bars
fig = plt.figure()
ax = fig.add_subplot(111)

svals = [s1, s2, s3, s4, s5, s6, s7]
rects1 = ax.bar(ind, svals, width, color='orangered')
wvals = [w1, w2, w3, w4, w5, w6, w7]
rects2 = ax.bar(ind+width, wvals, width, color='dodgerblue')
cvals = [c1, c2, c3, c4, c5, c6, c7]
rects3 = ax.bar(ind+width*2, cvals, width, color='darkgrey')
bvals = [b1, b2, b3, b4, b5, b6, b7]
rects4 = ax.bar(ind+width*3, bvals, width, color='seagreen')
evals = [e1, e2, e3, e4, e5, e6, e7]
rects5 = ax.bar(ind+width*4, evals, width, color='lime')

ax.set_ylabel('Installed capacities')
ax.set_xlabel('Yearly utilisation efficiency')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('70%', '75%', '80%', '85%', '90%', '95%', '100%') )
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







N = 7
ind = np.arange(N)  # the x locations for the groups
width = 0.3       # the width of the bars
fig = plt.figure()
ax = fig.add_subplot(111)

svals = [s1, s2, s3, s4, s5, s6, s7]
rects1 = ax.bar(ind, svals, width, color='orangered')
wvals = [w1, w2, w3, w4, w5, w6, w7]
rects2 = ax.bar(ind+width, wvals, width, color='dodgerblue')
cvals = [c1, c2, c3, c4, c5, c6, c7]
rects3 = ax.bar(ind+width*2, cvals, width, color='darkgrey')

ax.set_ylabel('Installed capacities [MW]')
ax.set_xlabel('Yearly utilisation efficiency [%]')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('70', '75', '80', '85', '90', '95', '100') )
ax.legend( (rects1[0], rects2[0], rects3[0]), ('Solar', 'Wind', 'Coal') , bbox_to_anchor=(0.0, 0.8, 1., .102))
def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1*h, '%d'%int(h),
                ha='center', va='bottom')
autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
plt.show()















# Revenue and cost distribution
data11 = pd.read_csv('Sensitivity/Util_yearly/Deterministic_util_yearly_yearly_0.7.csv')
data22 = pd.read_csv('Sensitivity/Util_yearly/Deterministic_util_yearly_yearly_0.75.csv')
data33 = pd.read_csv('Sensitivity/Util_yearly/Deterministic_util_yearly_yearly_0.8.csv')
data44 = pd.read_csv('Sensitivity/Util_yearly/Deterministic_util_yearly_yearly_0.85.csv')
data55 = pd.read_csv('Sensitivity/Util_yearly/Deterministic_util_yearly_yearly_0.9.csv')
data66 = pd.read_csv('Sensitivity/Util_yearly/Deterministic_util_yearly_yearly_0.95.csv')
data77 = pd.read_csv('Sensitivity/Util_yearly/Deterministic_util_yearly_yearly_1.csv')

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

p6 = data66['PPA revenue']
m6 = data66['market revenue']
c6 = (data66['OpexFix'])*(-1)
o6 = (data66['OpexVar'])*(-1)
f6 = (data66['ProdCost'])*(-1)
k6 = (data66['Penalty'])*(-1)

p7 = data77['PPA revenue']
m7 = data77['market revenue']
c7 = (data77['OpexFix'])*(-1)
o7 = (data77['OpexVar'])*(-1)
f7 = (data77['ProdCost'])*(-1)
k7 = (data77['Penalty'])*(-1)

x = ['70%', '75%', '80%', '85%', '90%', '95%', '100%']
y1 = np.array([sum(p1), sum(p2), sum(p3), sum(p4), sum(p5), sum(p6), sum(p7)])
y2 = np.array([sum(m1), sum(m2), sum(m3), sum(m4), sum(m5), sum(m6), sum(m7)])

# plot bars in stack manner
plt.bar(x, y1, color='limegreen')
plt.bar(x, y2, bottom=y1, color='springgreen')

x = ['70%', '75%', '80%', '85%', '90%', '95%', '100%']
y3 = np.array([sum(c1), sum(c2), sum(c3), sum(c4), sum(c5), sum(c6), sum(c7)])
y4 = np.array([sum(o1), sum(o2), sum(o3), sum(o4), sum(o5), sum(o6), sum(o7)])
y5 = np.array([sum(f1), sum(f2), sum(f3), sum(f4), sum(f5), sum(f6), sum(f7)])
y6 = np.array([sum(k1), sum(k2), sum(k3), sum(k4), sum(k5), sum(k6), sum(k7)])

# plot bars in stack manner
plt.bar(x, y3, color='midnightblue')
plt.bar(x, y4, bottom=y3, color='aqua')
plt.bar(x, y5, bottom=y3 + y4, color='dimgrey')
plt.bar(x, y6, bottom=y3 + y4 + y5, color='red')
plt.xlabel("Yearly utilisation efficiency")
plt.ylabel("Costs and revenues [€]")
plt.legend(['Revenue from PPA', 'Revenue from market', 'Fixed opex', 'Variable opex', 'Fuel cost', 'Penalty cost'])
plt.axhline(y=0, linewidth=1, color='black')
plt.show()

# Emissions
y = np.array([math.ceil(sum(data11['CO2'])), math.ceil(sum(data22['CO2'])), math.ceil(sum(data33['CO2'])),
              math.ceil(sum(data44['CO2'])), math.ceil(sum(data55['CO2'])), math.ceil(sum(data66['CO2'])),
              math.ceil(sum(data77['CO2']))])
x = ['70%', '75%', '80%', '85%', '90%', '95%', '100%']
fig, ax = plt.subplots()
width = 0.75
ind = np.arange(len(y))
ax.bar(x, y, width, color="lightslategrey")
for index, data in enumerate(y):
    plt.text(x=index, y=data+1, s=f"{data}", ha='center', va='bottom')
plt.xlabel('Yearly utilisation efficiency')
plt.ylabel('Tonnes of CO2')
plt.show()

# Energy production by source
data1 = pd.read_csv('Sensitivity/Util_yearly/Deterministic_util_yearly_hourly_0.7.csv')
data2 = pd.read_csv('Sensitivity/Util_yearly/Deterministic_util_yearly_hourly_0.75.csv')
data3 = pd.read_csv('Sensitivity/Util_yearly/Deterministic_util_yearly_hourly_0.8.csv')
data4 = pd.read_csv('Sensitivity/Util_yearly/Deterministic_util_yearly_hourly_0.85.csv')
data5 = pd.read_csv('Sensitivity/Util_yearly/Deterministic_util_yearly_hourly_0.9.csv')
data6 = pd.read_csv('Sensitivity/Util_yearly/Deterministic_util_yearly_hourly_0.95.csv')
data7 = pd.read_csv('Sensitivity/Util_yearly/Deterministic_util_yearly_hourly_1.csv')

x = ['70%', '75%', '80%', '85%', '90%', '95%', '100%']
y1 = np.array([sum(data1['solar']), sum(data2['solar']), sum(data3['solar']), sum(data4['solar']),
               sum(data5['solar']), sum(data6['solar']), sum(data7['solar'])])
y2 = np.array([sum(data1['wind']), sum(data2['wind']), sum(data3['wind']), sum(data4['wind']),
               sum(data5['wind']), sum(data6['wind']), sum(data7['wind'])])
y3 = np.array([sum(data1['coal']), sum(data2['coal']), sum(data3['coal']), sum(data4['coal']),
               sum(data5['coal']), sum(data6['coal']), sum(data7['coal'])])
y4 = np.array([sum(data1['battery']), sum(data2['battery']), sum(data3['battery']), sum(data4['battery']),
               sum(data5['battery']), sum(data6['battery']), sum(data7['battery'])])

# plot bars in stack manner
plt.bar(x, y1, color='orangered')
plt.bar(x, y2, bottom=y1, color='dodgerblue')
plt.bar(x, y3, bottom=y1 + y2, color='darkgrey')
plt.bar(x, y4, bottom=y1 + y2 + y3, color='seagreen')
plt.xlabel("Yearly utilisation efficiency")
plt.ylabel("Energy [MWh]")
plt.legend(['Solar', 'Wind', 'Coal', 'Battery'])
plt.show()



