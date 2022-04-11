import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data5 = pd.read_csv('Sensitivity/Future_electricity_price/Deterministic_future_elec_price_overall.csv')
s1 = data5['1.02'].loc[0]
s2 = data5['1.04'].loc[0]
s3 = data5['1.0609'].loc[0]
s4 = data5['1.08'].loc[0]
s5 = data5['1.1'].loc[0]
s6 = data5['1.12'].loc[0]
w1 = data5['1.02'].loc[1]
w2 = data5['1.04'].loc[1]
w3 = data5['1.0609'].loc[1]
w4 = data5['1.08'].loc[1]
w5 = data5['1.1'].loc[1]
w6 = data5['1.12'].loc[1]
c1 = data5['1.02'].loc[2]
c2 = data5['1.04'].loc[2]
c3 = data5['1.0609'].loc[2]
c4 = data5['1.08'].loc[2]
c5 = data5['1.1'].loc[2]
c6 = data5['1.12'].loc[2]
b1 = data5['1.02'].loc[3]
b2 = data5['1.04'].loc[3]
b3 = data5['1.0609'].loc[3]
b4 = data5['1.08'].loc[3]
b5 = data5['1.1'].loc[3]
b6 = data5['1.12'].loc[3]
e1 = data5['1.02'].loc[4]
e2 = data5['1.04'].loc[4]
e3 = data5['1.0609'].loc[4]
e4 = data5['1.08'].loc[4]
e5 = data5['1.1'].loc[4]
e6 = data5['1.12'].loc[4]

N = 6
ind = np.arange(N)  # the x locations for the groups
width = 0.2       # the width of the bars
fig = plt.figure()
ax = fig.add_subplot(111)

svals = [s1, s2, s3, s4, s5, s6]
rects1 = ax.bar(ind, svals, width, color='tab:red')
wvals = [w1, w2, w3, w4, w5, w6]
rects2 = ax.bar(ind+width, wvals, width, color='mediumblue')
cvals = [c1, c2, c3, c4, c5, c6]
rects3 = ax.bar(ind+width*2, cvals, width, color='darkslategrey')
bvals = [b1, b2, b3, b4, b5, b6]
rects4 = ax.bar(ind+width*3, bvals, width, color='green')
evals = [e1, e2, e3, e4, e5, e6]
rects5 = ax.bar(ind+width*4, evals, width, color='lime')

ax.set_ylabel('Installed capacities')
ax.set_xlabel('Future electricity price growth rate')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('2%', '4%', '6.09%', '8%', '10%', '12%') )
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
autolabel(rects4)
autolabel(rects5)
plt.show()


# Revenue and cost distribution
data11 = pd.read_csv('Sensitivity/Future_electricity_price/Deterministic_future_elec_price_yearly_1.02.csv')
data22 = pd.read_csv('Sensitivity/Future_electricity_price/Deterministic_future_elec_price_yearly_1.04.csv')
data33 = pd.read_csv('Sensitivity/Future_electricity_price/Deterministic_future_elec_price_yearly_1.0609.csv')
data44 = pd.read_csv('Sensitivity/Future_electricity_price/Deterministic_future_elec_price_yearly_1.08.csv')
data55 = pd.read_csv('Sensitivity/Future_electricity_price/Deterministic_future_elec_price_yearly_1.1.csv')
data66 = pd.read_csv('Sensitivity/Future_electricity_price/Deterministic_future_elec_price_yearly_1.12.csv')

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

x = ['2%', '4%', '6.09%', '8%', '10%', '12%']
y1 = np.array([sum(p1), sum(p2), sum(p3), sum(p4), sum(p5), sum(p6)])
y2 = np.array([sum(m1), sum(m2), sum(m3), sum(m4), sum(m5), sum(m6)])

# plot bars in stack manner
plt.bar(x, y1, color='lime')
plt.bar(x, y2, bottom=y1, color='mediumblue')
plt.xlabel("Future electricity price growth rate")
plt.ylabel("Energy [MWh]")
plt.legend(['revenue from PPA', 'revenue from market'])
plt.show()

x = ['2%', '4%', '6.09%', '8%', '10%', '12%']
y3 = np.array([sum(c1), sum(c2), sum(c3), sum(c4), sum(c5), sum(c6)])
y4 = np.array([sum(o1), sum(o2), sum(o3), sum(o4), sum(o5), sum(o6)])
y5 = np.array([sum(f1), sum(f2), sum(f3), sum(f4), sum(f5), sum(f6)])
y6 = np.array([sum(k1), sum(k2), sum(k3), sum(k4), sum(k5), sum(k6)])

# plot bars in stack manner
plt.bar(x, y3, color='green')
plt.bar(x, y4, bottom=y3, color='orange')
plt.bar(x, y5, bottom=y3 + y4, color='darkslategrey')
plt.bar(x, y6, bottom=y3 + y4 + y5, color='tab:red')
plt.xlabel("Future electricity price growth rate")
plt.ylabel("Energy [MWh]")
plt.legend(['fixed opex', 'variable opex', 'fuel cost', 'penalty cost'])
plt.show()

