import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data1 = pd.read_csv('Sensitivity/CO2_cost/Deterministic_CO2_cost_hourly_no_CO2_cost.csv')
data2 = pd.read_csv('Sensitivity/CO2_cost/Deterministic_CO2_cost_hourly_five_year_low.csv')
data3 = pd.read_csv('Sensitivity/CO2_cost/Deterministic_CO2_cost_hourly_five_year_medium.csv')
data4 = pd.read_csv('Sensitivity/CO2_cost/Deterministic_CO2_cost_hourly_continuous_high.csv')
data5 = pd.read_csv('Sensitivity/CO2_cost/Deterministic_CO2_cost_overall.csv')
s1 = data5['no_CO2_cost'].loc[0]
s2 = data5['five_year_low'].loc[0]
s3 = data5['five_year_medium'].loc[0]
s4 = data5['continuous_high'].loc[0]
w1 = data5['no_CO2_cost'].loc[1]
w2 = data5['five_year_low'].loc[1]
w3 = data5['five_year_medium'].loc[1]
w4 = data5['continuous_high'].loc[1]
c1 = data5['no_CO2_cost'].loc[2]
c2 = data5['five_year_low'].loc[2]
c3 = data5['five_year_medium'].loc[2]
c4 = data5['continuous_high'].loc[2]
b1 = data5['no_CO2_cost'].loc[3]
b2 = data5['five_year_low'].loc[3]
b3 = data5['five_year_medium'].loc[3]
b4 = data5['continuous_high'].loc[3]
e1 = data5['no_CO2_cost'].loc[4]
e2 = data5['five_year_low'].loc[4]
e3 = data5['five_year_medium'].loc[4]
e4 = data5['continuous_high'].loc[4]

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
ax.set_xlabel('CO2 cost')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('Case 0', 'Case 1', 'Case 2', 'Case 3') )
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

# Revenue and cost distribution
data11 = pd.read_csv('Sensitivity/CO2_cost/Deterministic_CO2_cost_yearly_no_CO2_cost.csv')
data22 = pd.read_csv('Sensitivity/CO2_cost/Deterministic_CO2_cost_yearly_five_year_low.csv')
data33 = pd.read_csv('Sensitivity/CO2_cost/Deterministic_CO2_cost_yearly_five_year_medium.csv')
data44 = pd.read_csv('Sensitivity/CO2_cost/Deterministic_CO2_cost_yearly_continuous_high.csv')

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

x = ['Case 0', 'Case 1', 'Case 2', 'Case 3']
y1 = np.array([sum(p1), sum(p2), sum(p3), sum(p4)])
y2 = np.array([sum(m1), sum(m2), sum(m3), sum(m4)])

# plot bars in stack manner
plt.bar(x, y1, color='limegreen')
plt.bar(x, y2, bottom=y1, color='springgreen')

x = ['Case 0', 'Case 1', 'Case 2', 'Case 3']
y3 = np.array([sum(c1), sum(c2), sum(c3), sum(c4)])
y4 = np.array([sum(o1), sum(o2), sum(o3), sum(o4)])
y5 = np.array([sum(f1), sum(f2), sum(f3), sum(f4)])
y6 = np.array([sum(k1), sum(k2), sum(k3), sum(k4)])

# plot bars in stack manner
plt.bar(x, y3, color='midnightblue')
plt.bar(x, y4, bottom=y3, color='aqua')
plt.bar(x, y5, bottom=y3 + y4, color='dimgrey')
plt.bar(x, y6, bottom=y3 + y4 + y5, color='red')
plt.xlabel("CO2 cost")
plt.ylabel("Costs and revenues [€]")
plt.legend(['Revenue from PPA', 'Revenue from market', 'Fixed opex', 'Variable opex', 'Fuel cost', 'Penalty cost'])
plt.axhline(y=0, linewidth=1, color='black')
plt.show()

