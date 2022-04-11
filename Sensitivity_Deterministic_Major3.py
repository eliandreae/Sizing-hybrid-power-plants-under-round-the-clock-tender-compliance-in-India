import pandas as pd
import Sensitivity_DeterministicV4_3 as Det

penalty_share_util_sensitivity_results = {}
for penalty_share_util in [0, 0.25, 1, 2, 3, 4, 5, 6]:
    print(f'Testing penalty_share_util {penalty_share_util}')
    results_hourly, results_yearly, optimal_capacities = Det.function(penalty_share_util=penalty_share_util)

    file22 = results_hourly.to_csv('Sensitivity/Penalty/Deterministic_penalty_share_util_hourly_'
                                   + str(penalty_share_util) + '.csv', index=False, header=True)
    file23 = results_yearly.to_csv('Sensitivity/Penalty/Deterministic_penalty_share_util_yearly_'
                                   + str(penalty_share_util) + '.csv', index=False, header=True)
    penalty_share_util_sensitivity_results[penalty_share_util] = optimal_capacities
penalty_share_util_sensitivity_df = pd.DataFrame.from_dict(penalty_share_util_sensitivity_results)
file24 = penalty_share_util_sensitivity_df.to_csv('Sensitivity/Penalty/Deterministic_penalty_share_util_overall.csv',
                                                  index=False, header=True)

penalty_share_ren_sensitivity_results = {}
for penalty_share_ren in [0, 0.25, 1, 2, 3, 4, 5, 6]:
    print(f'Testing penalty_share_ren {penalty_share_ren}')
    results_hourly, results_yearly, optimal_capacities = Det.function(penalty_share_ren=penalty_share_ren)

    file25 = results_hourly.to_csv('Sensitivity/Penalty/Deterministic_penalty_share_ren_hourly_'
                                   + str(penalty_share_ren) + '.csv', index=False, header=True)
    file26 = results_yearly.to_csv('Sensitivity/Penalty/Deterministic_penalty_share_ren_yearly_'
                                   + str(penalty_share_ren) + '.csv', index=False, header=True)
    penalty_share_ren_sensitivity_results[penalty_share_ren] = optimal_capacities
penalty_share_ren_sensitivity_df = pd.DataFrame.from_dict(penalty_share_ren_sensitivity_results)
file27 = penalty_share_ren_sensitivity_df.to_csv('Sensitivity/Penalty/Deterministic_penalty_share_ren_overall.csv',
                                                 index=False, header=True)