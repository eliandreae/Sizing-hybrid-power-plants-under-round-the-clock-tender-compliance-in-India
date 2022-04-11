import pandas as pd
import Sensitivity_Investment as Inv

tau_sensitivity_results = {}
for tau_s in [250, 500, 750, 1000]:
    print(f'Testing tau {tau_s}')
    results_hourly, results_yearly, optimal_capacities = Inv.function(tau_s=tau_s)

    file1 = results_hourly.to_csv('Sensitivity/Tender_bid/Investment_tender_hourly_' + str(tau_s) + '.csv',
                                  index=False, header=True)
    file2 = results_yearly.to_csv('Sensitivity/Tender_bid/Investment_tender_yearly_' + str(tau_s) + '.csv',
                                  index=False, header=True)
    tau_sensitivity_results[tau_s] = optimal_capacities
tau_sensitivity_df = pd.DataFrame.from_dict(tau_sensitivity_results)
file3 = tau_sensitivity_df.to_csv('Sensitivity/Tender_bid/Investment_tender_overall.csv', index=False, header=True)

bat_scale_sensitivity_results = {}
for bat_scale in [0.25, 0.5, 0.75, 0.9, 1]:
    print(f'Testing bat_scale {bat_scale}')
    results_hourly, results_yearly, optimal_capacities = Inv.function(bat_scale=bat_scale)

    file4 = results_hourly.to_csv('Sensitivity/Battery_cost/Investment_batScale_hourly_' + str(bat_scale) + '.csv',
                                  index=False, header=True)
    file5 = results_yearly.to_csv('Sensitivity/Battery_cost/Investment_batScale_yearly_' + str(bat_scale) + '.csv',
                                  index=False, header=True)
    bat_scale_sensitivity_results[bat_scale] = optimal_capacities
bat_scale_sensitivity_df = pd.DataFrame.from_dict(bat_scale_sensitivity_results)
file6 = bat_scale_sensitivity_df.to_csv('Sensitivity/Battery_cost/Investment_batScale_overall.csv',
                                        index=False, header=True)

d_rate_sensitivity_results = {}
for d_rate in [0.04, 0.06, 0.08, 0.1, 0.11, 0.12, 0.15, 0.2]:
    print(f'Testing utilisation_eff {d_rate}')
    results_hourly, results_yearly, optimal_capacities = Inv.function(d_rate=d_rate)

    file19 = results_hourly.to_csv('Sensitivity/Discount_rate/Investment_d_rate_hourly_'
                                   + str(d_rate) + '.csv', index=False, header=True)
    file20 = results_yearly.to_csv('Sensitivity/Discount_rate/Investment_d_rate_yearly_'
                                   + str(d_rate) + '.csv', index=False, header=True)
    d_rate_sensitivity_results[d_rate] = optimal_capacities
d_rate_sensitivity_df = pd.DataFrame.from_dict(d_rate_sensitivity_results)
file21 = d_rate_sensitivity_df.to_csv('Sensitivity/Discount_rate/Investment_d_rate_overall.csv',
                                      index=False, header=True)