import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# Revenue and cost distribution
data11 = pd.read_csv('Results_HPC/Results_Stochastic_yearly_HPC.csv')
data11 = data11.sort_values('scenario')
data11 = data11.reset_index(drop=True)
data11_1 = data11.loc[0:29]
data11_2 = data11.loc[30:59]
data22 = pd.read_csv('Results_HPC/Results_Stochastic_scen3_yearly_HPC.csv')
data22 = data22.sort_values('scenario')
data22 = data22.reset_index(drop=True)
data22_1 = data22.loc[0:29]
data22_2 = data22.loc[30:59]
data22_3 = data22.loc[60:89]
data33 = pd.read_csv('Results_HPC/Results_Deterministic_yearly_HPC.csv')

# Emissions
x = ['Det', 'Scen 2.1', 'Scen 2.2', 'Scen 3.1', 'Scen 3.2', 'Scen 3.3']
y1 = np.array([sum(data33['CO2']), sum(data11_1['CO2']), sum(data11_2['CO2']),
               sum(data22_1['CO2']), sum(data22_2['CO2']), sum(data22_3['CO2'])])
plt.bar(x, y1, color='lightslategrey')
plt.ylabel("Tonnes of CO2")
plt.show()



