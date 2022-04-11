import pandas as pd
import Sensitivity_DeterministicV4 as Det
import Sensitivity_DeterministicV4_3 as Det3

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

penalty_share_ren_sensitivity_results = {}
for penalty_share_ren in [0, 0.25, 1, 2, 3, 4, 5, 6]:
    print(f'Testing penalty_share_ren {penalty_share_ren}')
    results_hourly, results_yearly, optimal_capacities = Det3.function(penalty_share_ren=penalty_share_ren)

    file25 = results_hourly.to_csv('Sensitivity/Penalty/Deterministic_penalty_share_ren_hourly_'
                                   + str(penalty_share_ren) + '.csv', index=False, header=True)
    file26 = results_yearly.to_csv('Sensitivity/Penalty/Deterministic_penalty_share_ren_yearly_'
                                   + str(penalty_share_ren) + '.csv', index=False, header=True)
    penalty_share_ren_sensitivity_results[penalty_share_ren] = optimal_capacities
penalty_share_ren_sensitivity_df = pd.DataFrame.from_dict(penalty_share_ren_sensitivity_results)
file27 = penalty_share_ren_sensitivity_df.to_csv('Sensitivity/Penalty/Deterministic_penalty_share_ren_overall.csv',
                                                 index=False, header=True)