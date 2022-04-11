import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data5 = pd.read_csv('Sensitivity/Renewable_share/Deterministic_renew_overall.csv')
s1 = data5['0.3'].loc[0]
s2 = data5['0.35'].loc[0]
s3 = data5['0.4'].loc[0]
s4 = data5['0.45'].loc[0]
s5 = data5['0.51'].loc[0]
s6 = data5['0.55'].loc[0]
s7 = data5['0.6'].loc[0]
s8 = data5['0.65'].loc[0]
s9 = data5['0.7'].loc[0]

w1 = data5['0.3'].loc[1]
w2 = data5['0.35'].loc[1]
w3 = data5['0.4'].loc[1]
w4 = data5['0.45'].loc[1]
w5 = data5['0.51'].loc[1]
w6 = data5['0.55'].loc[1]
w7 = data5['0.6'].loc[1]
w8 = data5['0.65'].loc[1]
w9 = data5['0.7'].loc[1]

c1 = data5['0.3'].loc[2]
c2 = data5['0.35'].loc[2]
c3 = data5['0.4'].loc[2]
c4 = data5['0.45'].loc[2]
c5 = data5['0.51'].loc[2]
c6 = data5['0.55'].loc[2]
c7 = data5['0.6'].loc[2]
c8 = data5['0.65'].loc[2]
c9 = data5['0.7'].loc[2]

b1 = data5['0.3'].loc[3]
b2 = data5['0.35'].loc[3]
b3 = data5['0.4'].loc[3]
b4 = data5['0.45'].loc[3]
b5 = data5['0.51'].loc[3]
b6 = data5['0.55'].loc[3]
b7 = data5['0.6'].loc[3]
b8 = data5['0.65'].loc[3]
b9 = data5['0.7'].loc[3]

e1 = data5['0.3'].loc[4]
e2 = data5['0.35'].loc[4]
e3 = data5['0.4'].loc[4]
e4 = data5['0.45'].loc[4]
e5 = data5['0.51'].loc[4]
e6 = data5['0.55'].loc[4]
e7 = data5['0.6'].loc[4]
e8 = data5['0.65'].loc[4]
e9 = data5['0.7'].loc[4]

N = 9
ind = np.arange(N)  # the x locations for the groups
width = 0.15       # the width of the bars
fig = plt.figure()
ax = fig.add_subplot(111)

svals = [s1, s2, s3, s4, s5, s6, s7, s8, s9]
rects1 = ax.bar(ind, svals, width, color='tab:red')
wvals = [w1, w2, w3, w4, w5, w6, w7, w8, w9]
rects2 = ax.bar(ind+width, wvals, width, color='mediumblue')
cvals = [c1, c2, c3, c4, c5, c6, c7, c8, c9]
rects3 = ax.bar(ind+width*2, cvals, width, color='darkslategrey')
bvals = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
rects4 = ax.bar(ind+width*3, bvals, width, color='green')
evals = [e1, e2, e3, e4, e5, e6, e7, e8, e9]
rects5 = ax.bar(ind+width*4, evals, width, color='lime')

ax.set_ylabel('Installed capacities')
ax.set_xlabel('Yearly renewable share')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('30%', '35%', '40%', '45%', '51%', '55%', '60%', '65%', '70%') )
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