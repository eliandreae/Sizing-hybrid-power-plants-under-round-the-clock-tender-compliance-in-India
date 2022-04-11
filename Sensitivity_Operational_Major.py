import Sensitivity_Operational as Ope

for tau_s in [250, 500, 750, 1000]:
    print(f'Testing tau {tau_s}')
    results_hourly, results_yearly, objective = Ope.function1(tau_s=tau_s)

    file1 = results_hourly.to_csv('Sensitivity/Tender_bid/Operational_tender_hourly_HPC_' + str(tau_s) + '.csv',
                                  index=True, header=True)
    file2 = results_yearly.to_csv('Sensitivity/Tender_bid/Operational_tender_yearly_HPC_' + str(tau_s) + '.csv',
                                  index=True, header=True)
    file3 = objective.to_csv('Sensitivity/Tender_bid/Operational_tender_objective_HPC_' + str(tau_s) + '.csv',
                             index=True, header=True)

for solar_max in [0, 100, 200, 300, 400, 500]:
    print(f'Testing solar_max {solar_max}')
    results_hourly, results_yearly, objective = Ope.function1(solar_max=solar_max)

    file7 = results_hourly.to_csv('Sensitivity/Capacity_max/Operational_solar_max_hourly_HPC_' + str(solar_max)
                                  + '.csv', index=True, header=True)
    file8 = results_yearly.to_csv('Sensitivity/Capacity_max/Operational_solar_max_yearly_HPC_' + str(solar_max)
                                  + '.csv', index=True, header=True)
    file9 = objective.to_csv('Sensitivity/Capacity_max/Operational_solar_max_objective_HPC_' + str(solar_max)
                             + '.csv', index=True, header=True)

for wind_max in [0, 100, 200, 300, 400, 500, 600]:
    print(f'Testing wind_max {wind_max}')
    results_hourly, results_yearly, objective = Ope.function1(wind_max=wind_max)

    file10 = results_hourly.to_csv('Sensitivity/Capacity_max/Operational_wind_max_hourly_HPC_' + str(wind_max) + '.csv',
                                   index=True, header=True)
    file11 = results_yearly.to_csv('Sensitivity/Capacity_max/Operational_wind_max_yearly_HPC_' + str(wind_max) + '.csv',
                                   index=True, header=True)
    file12 = objective.to_csv('Sensitivity/Capacity_max/Operational_wind_max_objective_HPC_' + str(wind_max) + '.csv',
                              index=True, header=True)

for coal_max in [0, 50, 100, 150, 200, 250, 300]:
    print(f'Testing coal_max {coal_max}')
    results_hourly, results_yearly, objective = Ope.function1(coal_max=coal_max)

    file13 = results_hourly.to_csv('Sensitivity/Capacity_max/Operational_coal_max_hourly_HPC_' + str(coal_max) + '.csv',
                                   index=True, header=True)
    file14 = results_yearly.to_csv('Sensitivity/Capacity_max/Operational_coal_max_yearly_HPC_' + str(coal_max) + '.csv',
                                   index=True, header=True)
    file15 = objective.to_csv('Sensitivity/Capacity_max/Operational_coal_max_objective_HPC_' + str(coal_max) + '.csv',
                              index=True, header=True)

for battery_max in [0, 50, 100, 150, 200, 250, 300]:
    print(f'Testing battery_max {battery_max}')
    results_hourly, results_yearly, objective = Ope.function1(battery_max=battery_max)

    file16 = results_hourly.to_csv('Sensitivity/Capacity_max/Operational_battery_max_hourly_HPC_' + str(battery_max)
                                   + '.csv', index=True, header=True)
    file17 = results_yearly.to_csv('Sensitivity/Capacity_max/Operational_battery_max_yearly_HPC_' + str(battery_max)
                                   + '.csv', index=True, header=True)
    file18 = objective.to_csv('Sensitivity/Capacity_max/Operational_battery_max_objective_HPC_' + str(battery_max)
                              + '.csv', index=True, header=True)

for energy_max in [0, 50, 100, 150, 200, 250, 300]:
    print(f'Testing energy_max {energy_max}')
    results_hourly, results_yearly, objective = Ope.function1(energy_max=energy_max)

    file19 = results_hourly.to_csv('Sensitivity/Capacity_max/Operational_energy_max_hourly_HPC_' + str(energy_max)
                                   + '.csv', index=True, header=True)
    file20 = results_yearly.to_csv('Sensitivity/Capacity_max/Operational_energy_max_yearly_HPC_' + str(energy_max)
                                   + '.csv', index=True, header=True)
    file21 = objective.to_csv('Sensitivity/Capacity_max/Operational_energy_max_objective_HPC_' + str(energy_max)
                              + '.csv', index=True, header=True)
