import pandas as pd
import Sensitivity_DeterministicV4 as Det

tau_sensitivity_results = {}
for tau_s in [250, 500, 750, 1000]:
    print(f'Testing tau {tau_s}')
    results_hourly, results_yearly, optimal_capacities = Det.function(tau_s=tau_s)

    file1 = results_hourly.to_csv('Sensitivity/Tender_bid/Deterministic_tender_hourly_' + str(tau_s) + '.csv',
                                  index=False, header=True)
    file2 = results_yearly.to_csv('Sensitivity/Tender_bid/Deterministic_tender_yearly_' + str(tau_s) + '.csv',
                                  index=False, header=True)
    tau_sensitivity_results[tau_s] = optimal_capacities
tau_sensitivity_df = pd.DataFrame.from_dict(tau_sensitivity_results)
file3 = tau_sensitivity_df.to_csv('Sensitivity/Tender_bid/Deterministic_tender_overall.csv',
                                  index=False, header=True)

bat_scale_sensitivity_results = {}
for bat_scale in [0.25, 0.5, 0.75, 0.9, 1]:
    print(f'Testing bat_scale {bat_scale}')
    results_hourly, results_yearly, optimal_capacities = Det.function(bat_scale=bat_scale)

    file4 = results_hourly.to_csv('Sensitivity/Battery_cost/Deterministic_batScale_hourly_' + str(bat_scale) + '.csv',
                                  index=False, header=True)
    file5 = results_yearly.to_csv('Sensitivity/Battery_cost/Deterministic_batScale_yearly_' + str(bat_scale) + '.csv',
                                  index=False, header=True)
    bat_scale_sensitivity_results[bat_scale] = optimal_capacities
bat_scale_sensitivity_df = pd.DataFrame.from_dict(bat_scale_sensitivity_results)
file6 = bat_scale_sensitivity_df.to_csv('Sensitivity/Battery_cost/Deterministic_batScale_overall.csv',
                                        index=False, header=True)

renew_yearly_sensitivity_results = {}
for renew_yearly in [0.3, 0.35, 0.4, 0.45, 0.51, 0.55, 0.6, 0.65, 0.7]:
    print(f'Testing renew_yearly {renew_yearly}')
    results_hourly, results_yearly, optimal_capacities = Det.function(renew_yearly=renew_yearly)

    file13 = results_hourly.to_csv('Sensitivity/Renewable_share/Deterministic_renew_hourly_' + str(renew_yearly)
                                   + '.csv', index=False, header=True)
    file14 = results_yearly.to_csv('Sensitivity/Renewable_share/Deterministic_renew_yearly_' + str(renew_yearly)
                                   + '.csv', index=False, header=True)
    renew_yearly_sensitivity_results[renew_yearly] = optimal_capacities
renew_yearly_sensitivity_df = pd.DataFrame.from_dict(renew_yearly_sensitivity_results)
file15 = renew_yearly_sensitivity_df.to_csv('Sensitivity/Renewable_share/Deterministic_renew_overall.csv',
                                            index=False, header=True)

util_eff_yearly_sensitivity_results = {}
for util_eff_yearly in [0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1]:
    print(f'Testing util_eff_yearly {util_eff_yearly}')
    results_hourly, results_yearly, optimal_capacities = Det.function(util_eff_yearly=util_eff_yearly)

    file16 = results_hourly.to_csv('Sensitivity/Util_yearly/Deterministic_util_yearly_hourly_'
                                   + str(util_eff_yearly) + '.csv', index=False, header=True)
    file17 = results_yearly.to_csv('Sensitivity/Util_yearly/Deterministic_util_yearly_yearly_'
                                   + str(util_eff_yearly) + '.csv', index=False, header=True)
    util_eff_yearly_sensitivity_results[util_eff_yearly] = optimal_capacities
util_eff_yearly_sensitivity_df = pd.DataFrame.from_dict(util_eff_yearly_sensitivity_results)
file18 = util_eff_yearly_sensitivity_df.to_csv('Sensitivity/Util_yearly/Deterministic_util_yearly_overall.csv',
                                               index=False, header=True)

d_rate_sensitivity_results = {}
for d_rate in [0.04, 0.06, 0.08, 0.1, 0.11, 0.12, 0.15, 0.2]:
    print(f'Testing d_rate {d_rate}')
    results_hourly, results_yearly, optimal_capacities = Det.function(d_rate=d_rate)

    file19 = results_hourly.to_csv('Sensitivity/Discount_rate/Deterministic_d_rate_hourly_'
                                   + str(d_rate) + '.csv', index=False, header=True)
    file20 = results_yearly.to_csv('Sensitivity/Discount_rate/Deterministic_d_rate_yearly_'
                                   + str(d_rate) + '.csv', index=False, header=True)
    d_rate_sensitivity_results[d_rate] = optimal_capacities
d_rate_sensitivity_df = pd.DataFrame.from_dict(d_rate_sensitivity_results)
file21 = d_rate_sensitivity_df.to_csv('Sensitivity/Discount_rate/Deterministic_d_rate_overall.csv',
                                      index=False, header=True)

