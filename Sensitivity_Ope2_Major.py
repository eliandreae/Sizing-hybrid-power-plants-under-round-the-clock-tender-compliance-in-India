import Sensitivity_Ope2 as Ope

for renew_max in [0, 100, 200, 300, 400, 500]:
    print(f'Testing renew_max {renew_max}')
    results_hourly, results_yearly, objective = Ope.function1(renew_max=renew_max)

    file7 = results_hourly.to_csv('Sensitivity/Capacity_max/Operational_renew_max_hourly_HPC_' + str(renew_max)
                                  + '.csv', index=True, header=True)
    file8 = results_yearly.to_csv('Sensitivity/Capacity_max/Operational_renew_max_yearly_HPC_' + str(renew_max)
                                  + '.csv', index=True, header=True)
    file9 = objective.to_csv('Sensitivity/Capacity_max/Operational_renew_max_objective_HPC_' + str(renew_max)
                             + '.csv', index=True, header=True)
