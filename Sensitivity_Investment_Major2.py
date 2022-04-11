import pandas as pd
import Sensitivity_Investment2 as Inv
from clean_data_NEW import get_clean_data
Nyears = 30
all_data, Ts, Y, Yp, Years, Hours_in_year = get_clean_data(Nyears)

CO2_cost_sensitivity_results = {}
c0 = [0] * 30
c1 = [0, 0, 0, 0, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15, 20, 20, 20, 20, 20, 20, 25, 25, 25, 25, 25]
c2 = [0, 0, 0, 0, 5, 5, 5, 5, 5, 7, 7, 7, 7, 7, 10, 10, 10, 10, 10, 10, 12, 12, 12, 12, 12, 12, 15, 15, 15, 15]
c3 = [0, 0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

case0 = {y: c0[Yp[y]] for y in Years}
case1 = {y: c1[Yp[y]] for y in Years}
case2 = {y: c2[Yp[y]] for y in Years}
case3 = {y: c3[Yp[y]] for y in Years}

cases = {'no_CO2_cost': case0, 'five_year_medium': case1, 'five_year_low': case2, 'continuous_high': case3}

for case_label, CO2_cost in cases.items():
    print(f'Testing bat_scale {case_label}')
    results_hourly, results_yearly, optimal_capacities = Inv.function(CO2_cost=CO2_cost)

    file1 = results_hourly.to_csv('Sensitivity/CO2_cost/Investment_CO2_cost_hourly_' + str(case_label) + '.csv',
                                  index=False, header=True)
    file2 = results_yearly.to_csv('Sensitivity/CO2_cost/Investment_CO2_cost_yearly_' + str(case_label) + '.csv',
                                  index=False, header=True)
    CO2_cost_sensitivity_results[case_label] = optimal_capacities
CO2_cost_sensitivity_df = pd.DataFrame.from_dict(CO2_cost_sensitivity_results)
file3 = CO2_cost_sensitivity_df.to_csv('Sensitivity/CO2_cost/Investment_CO2_cost_overall.csv',
                                       index=False, header=True)
# raise SystemExit

# Future electricity prices (inflation rate)
future_elec_price_change_sensitivity_results = {}
for future_elec_price_change in [1.02, 1.04, 1.0609, 1.08, 1.1, 1.12]:
    print(f'Testing bat_scale {future_elec_price_change}')
    results_hourly, results_yearly, optimal_capacities = Inv.function(future_elec_price_change=future_elec_price_change)

    file4 = results_hourly.to_csv('Sensitivity/Future_electricity_price/Investment_future_elec_price_hourly_'
                                  + str(future_elec_price_change) + '.csv', index=False, header=True)
    file5 = results_yearly.to_csv('Sensitivity/Future_electricity_price/Investment_future_elec_price_yearly_'
                                  + str(future_elec_price_change) + '.csv', index=False, header=True)
    future_elec_price_change_sensitivity_results[future_elec_price_change] = optimal_capacities
future_elec_price_change_sensitivity_df = pd.DataFrame.from_dict(future_elec_price_change_sensitivity_results)
file6 = future_elec_price_change_sensitivity_df.to_csv('Sensitivity/Future_electricity_price/'
                                                       'Investment_future_elec_price_overall.csv',
                                                       index=False, header=True)

# PPA cyclic evaluation of LCOE
PPA_init_sensitivity_results = {}
for PPA_init in [30, 50, 70, 90, 110, 130]:
    print(f'Testing bat_scale {PPA_init}')
    results_hourly, results_yearly, optimal_capacities = Inv.function(PPA_init=PPA_init)

    file7 = results_hourly.to_csv('Sensitivity/PPA/Investment_PPA_init_hourly_' + str(PPA_init) + '.csv',
                                  index=False, header=True)
    file8 = results_yearly.to_csv('Sensitivity/PPA/Investment_PPA_init_yearly_' + str(PPA_init) + '.csv',
                                  index=False, header=True)
    PPA_init_sensitivity_results[PPA_init] = optimal_capacities
PPA_init_sensitivity_df = pd.DataFrame.from_dict(PPA_init_sensitivity_results)
file9 = PPA_init_sensitivity_df.to_csv('Sensitivity/PPA/Investment_PPA_init_overall.csv', index=False, header=True)
