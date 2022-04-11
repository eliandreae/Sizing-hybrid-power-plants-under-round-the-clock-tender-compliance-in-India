import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data15 = pd.read_csv('Sensitivity/Battery_cost/Deterministic_batScale_overall.csv')
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
rects1 = ax.bar(ind, svals, width, color='tab:red')
wvals = [w1, w2, w3, w4, w5]
rects2 = ax.bar(ind+width, wvals, width, color='mediumblue')
cvals = [c1, c2, c3, c4, c5]
rects3 = ax.bar(ind+width*2, cvals, width, color='darkslategrey')
bvals = [b1, b2, b3, b4, b4]
rects4 = ax.bar(ind+width*3, bvals, width, color='green')
evals = [e1, e2, e3, e4, e5]
rects5 = ax.bar(ind+width*4, evals, width, color='lime')

ax.set_ylabel('Installed capacities')
ax.set_xlabel('Battery cost scale')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('0.25', '0.5', '0.75', '0.9', '1.0') )
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



