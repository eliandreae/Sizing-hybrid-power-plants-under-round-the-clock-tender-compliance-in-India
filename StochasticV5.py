import pyomo.environ as pyo
from itertools import islice
import pandas as pd
import numpy as np

Nyears = 30
Nscenarios = 2
from clean_data_NEW import get_clean_data
all_data, Ts, Y, Yp, Years, Hours_in_year = get_clean_data(Nyears)
from parameters_NEW import Parameters
CFsolar, CFwind, prices, tau, PPA, penalty_utilization_yearly, penalty_renewable,\
           Cmin, eta_round, SoCmin, SoCmax, cycles, deg_per_hour, coalCO2Emis, eta_fuel, solarC, windC, coalFuelC, \
           chargeC, solarOpexVar, windOpexVar, coalOpexVar, coalEmisC, batteryOpexVar, solarOpexFix, windOpexFix, \
           coalOpexFix, batteryOpexFix, EOpexFix, solarCapex, windCapex, coalCapex, batteryCapex, BOS, ECapex, GC, r, \
           util_yearly, renew_share, PPA_dyn, penalty_utilization_yearly_dyn, penalty_renewable_dyn, \
           opex_refurbish_bat, opex_refurbish_E, init = Parameters(Nyears)

from parameters_NEW import Scenarios
S, Prob = Scenarios(Nscenarios)
from parameters_NEW import ShuffleCFs

CFwinds = {}
CFsolars = {}
years_In_Scenario = {}
Prices = {}
coalFuelCs = {}

for s in S:
    newCFwind, newCFsolar, shuffleYear, newPrices, newCoalFuelC = ShuffleCFs(CFwind, CFsolar, prices, coalFuelC, Nyears,
                                                                             local_Hours_in_year=Hours_in_year)
    CFwinds[s] = newCFwind
    CFsolars[s] = newCFsolar
    years_In_Scenario[s] = shuffleYear
    Prices[s] = newPrices
    coalFuelCs[s] = np.concatenate([newCoalFuelC, newCoalFuelC])

print(years_In_Scenario)

Historical_Time_Scenario = {s: [h for ys in years_In_Scenario[s] for h in Hours_in_year[ys]] for s in S}

########################################################################################################################
# Simulation of one year

def Stochastic():
    m = pyo.ConcreteModel()

    m.solarP = pyo.Var(Ts, S, domain=pyo.NonNegativeReals)
    m.windP = pyo.Var(Ts, S, domain=pyo.NonNegativeReals)
    m.coalP = pyo.Var(Ts, S, domain=pyo.NonNegativeReals)
    m.batteryP = pyo.Var(Ts, S, domain=pyo.Reals)
    m.chargeP = pyo.Var(Ts, S, domain=pyo.NonNegativeReals)
    m.dischargeP = pyo.Var(Ts, S, domain=pyo.NonNegativeReals)
    m.E = pyo.Var(Ts, S, domain=pyo.Reals)

    m.totProd = pyo.Var(Ts, S, domain=pyo.NonNegativeReals)
    m.tenderProd = pyo.Var(Ts, S, domain=pyo.NonNegativeReals)
    m.aboveProd = pyo.Var(Ts, S, domain=pyo.NonNegativeReals)

    m.CO2Emis = pyo.Var(Ts, S, domain=pyo.NonNegativeReals)

    m.e_nonDel_yearly = pyo.Var(Years, S, domain=pyo.NonNegativeReals)
    m.e_renew_share = pyo.Var(Years, S, domain=pyo.NonNegativeReals)

    m.solarPmax = pyo.Var(domain=pyo.NonNegativeReals)
    m.windPmax = pyo.Var(domain=pyo.NonNegativeReals)
    m.coalPmax = pyo.Var(domain=pyo.NonNegativeReals, bounds=(0, tau))
    m.batteryPmax = pyo.Var(domain=pyo.NonNegativeReals, bounds=(0, tau))
    m.Emax = pyo.Var(domain=pyo.NonNegativeReals)

    m.Capex = pyo.Var(domain=pyo.NonNegativeReals)
    m.OpexFix = pyo.Var(Years, domain=pyo.NonNegativeReals)
    m.OpexVar = pyo.Var(Years, S, domain=pyo.NonNegativeReals)
    m.Prod = pyo.Var(Years, S, domain=pyo.NonNegativeReals)
    m.Revenue = pyo.Var(Years, S, domain=pyo.Reals)
    m.Penalty = pyo.Var(Years, S, domain=pyo.Reals)

    m.present_value = pyo.Var(Years, S, domain=pyo.Reals)
    m.free_cash_flow = pyo.Var(Years, S, domain=pyo.Reals)

    # Objective - Maximise NPV
    m.NPV = pyo.Objective(expr=sum(Prob[s] * sum((1 / pow((1 + r), Y[year])) * (m.Revenue[year, s] - m.Prod[year, s]
                          - m.OpexVar[year, s] - m.OpexFix[year] - m.Penalty[year, s]) for year in Years) for s in S)
                          - m.Capex,
                          sense=pyo.maximize)

    m.PresentValue = pyo.ConstraintList()
    for s in S:
        for year in Years:
            m.PresentValue.add((1 / pow((1 + r), Y[year])) * (m.Revenue[year, s] - m.Prod[year, s] - m.OpexVar[year, s]
                                                              - m.OpexFix[year] - m.Penalty[year, s])
                               == m.present_value[year, s])

    m.FreeCashFlow = pyo.ConstraintList()
    for s in S:
        for year in Years:
            m.FreeCashFlow.add(m.Revenue[year, s] - m.Prod[year, s] - m.OpexVar[year, s] - m.OpexFix[year]
                               - m.Penalty[year, s] == m.free_cash_flow[year, s])

    m.CAPEX = pyo.Constraint(
        rule=lambda m:
        solarCapex * m.solarPmax
        + windCapex * m.windPmax
        + coalCapex * m.coalPmax
        + batteryCapex * m.batteryPmax
        + ECapex * m.Emax
        + BOS * m.batteryPmax
        == m.Capex)

    m.OPEXfix = pyo.ConstraintList()
    for year in Years:
        m.OPEXfix.add(solarOpexFix[year] * m.solarPmax
                      + windOpexFix[year] * m.windPmax
                      + coalOpexFix[year] * m.coalPmax
                      + batteryOpexFix[year] * m.batteryPmax
                      + EOpexFix[year] * m.Emax
                      + opex_refurbish_bat[year] * m.batteryPmax
                      + opex_refurbish_E[year] * m.Emax
                      <= m.OpexFix[year])

    m.OPEXvar = pyo.ConstraintList()
    m.PROD = pyo.ConstraintList()
    m.REVENUE = pyo.ConstraintList()
    m.PENALTY1 = pyo.ConstraintList()
    m.PENALTY2 = pyo.ConstraintList()
    for s in S:
        for year in Years:
            m.OPEXvar.add(pyo.quicksum(solarOpexVar * m.solarP[t, s]
                                       + windOpexVar * m.windP[t, s]
                                       + coalOpexVar * m.coalP[t, s]
                                       + batteryOpexVar * m.batteryP[t, s] for t in Hours_in_year[year])
                          <= m.OpexVar[year, s])

            m.PROD.add(pyo.quicksum(solarC * m.solarP[t, s]
                                    + windC * m.windP[t, s]
                                    + ((coalFuelCs[s][Historical_Time_Scenario[s][t-1]]
                                        + coalEmisC * coalCO2Emis) / eta_fuel) * m.coalP[t, s]
                                    + chargeC * m.batteryP[t, s] for t in Hours_in_year[year])
                       <= m.Prod[year, s])

            m.REVENUE.add(pyo.quicksum(Prices[s][Historical_Time_Scenario[s][t-1]] * m.aboveProd[t, s]
                                       + PPA_dyn[year] * m.tenderProd[t, s] for t in Hours_in_year[year])
                          >= m.Revenue[year, s])

            # Pay the largest penalty
            m.PENALTY1.add(penalty_utilization_yearly_dyn[year] * m.e_nonDel_yearly[year, s] <= m.Penalty[year, s])
            m.PENALTY2.add(penalty_renewable_dyn[year] * m.e_renew_share[year, s] <= m.Penalty[year, s])

    # Grid-constrained capacity
    m.grid = pyo.Constraint(Ts, S, rule=lambda m, t, s: m.solarP[t, s] + m.windP[t, s] + m.batteryP[t, s] <= GC)

    print(f"Ts: {len(Ts)}")
    print(f"CFsolars: {[len(v) for v in CFsolars.values()]}")

    # Renewable production capacity
    m.PV = pyo.Constraint(
        Ts, S, rule=lambda m, t, s:
        m.solarP[t, s] <= float(CFsolars[s][Historical_Time_Scenario[s][t - 1]]) * m.solarPmax)
    m.Turbine = pyo.Constraint(
        Ts, S, rule=lambda m, t, s:
        m.windP[t, s] <= float(CFwinds[s][Historical_Time_Scenario[s][t - 1]]) * m.windPmax)

    # Coal has to stay on-line all the time due to technical limitations
    m.coalOnline = pyo.Constraint(Ts, S, rule=lambda m, t, s: m.coalP[t, s] >= Cmin * m.coalPmax)
    m.coalMax = pyo.Constraint(Ts, S, rule=lambda m, t, s: m.coalP[t, s] <= m.coalPmax)

    # Tons of C02 emissions from coal
    m.Emissions = pyo.Constraint(Ts, S, rule=lambda m, t, s: coalCO2Emis * m.coalP[t, s] == m.CO2Emis[t, s])

    # Battery production
    m.batMin = pyo.Constraint(Ts, S, rule=lambda m, t, s: m.batteryP[t, s] >= -m.batteryPmax)
    m.batMax = pyo.Constraint(Ts, S, rule=lambda m, t, s: m.batteryP[t, s] <= m.batteryPmax)
    m.batCharge = pyo.Constraint(Ts, S, rule=lambda m, t, s: m.chargeP[t, s] <= m.batteryPmax)
    m.batDischarge = pyo.Constraint(Ts, S, rule=lambda m, t, s: m.dischargeP[t, s] <= m.batteryPmax)
    m.bat = pyo.Constraint(Ts, S, rule=lambda m, t, s: m.batteryP[t, s] == m.dischargeP[t, s] - m.chargeP[t, s])

    # Battery is charged by renewable power
    m.batRenewable = pyo.Constraint(Ts, S, rule=lambda m, t, s: m.chargeP[t, s] <= m.solarP[t, s] + m.windP[t, s])

    # State of Charge - battery energy
    m.SoC_lower = pyo.Constraint(Ts, S, rule=lambda m, t, s: m.E[t, s] >= SoCmin * m.Emax)
    m.SoC_upper = pyo.Constraint(Ts, S, rule=lambda m, t, s: m.E[t, s] <= SoCmax * m.Emax)
    m.EnergyZero = pyo.Constraint(S, rule=lambda m, S: m.E[Ts[0], s] == init * m.Emax)
    m.Energy = pyo.ConstraintList()
    for s in S:
        for t, tneg1 in zip(islice(Ts, 1, None), Ts):
            m.Energy.add(m.E[t, s] == m.E[tneg1, s] + eta_round * m.chargeP[t, s] - m.dischargeP[t, s])

    # Battery degradation over years
    m.degradation = pyo.ConstraintList()
    for s in S:
        for year in Years:
            for t in Hours_in_year[year]:
                degradationfactor = max(0.9, (1 - deg_per_hour * t))
                m.degradation.add(m.Emax * degradationfactor >= m.E[t, s])

    # Limit the use of battery cycles to 365 each year
    m.cycleLife = pyo.ConstraintList()
    for s in S:
        for year in Years:
            m.cycleLife.add(pyo.quicksum(m.dischargeP[t, s] for t in Hours_in_year[year]) <= cycles * m.batteryPmax)

    # Tender production and above
    m.deliverTender = pyo.Constraint(Ts, S, rule=lambda m, t, s: m.tenderProd[t, s] <= tau)
    m.limitTender = pyo.Constraint(Ts, S, rule=lambda m, t, s: m.tenderProd[t, s] <= m.totProd[t, s])
    m.aboveTender = pyo.Constraint(
        Ts, S, rule=lambda m, t, s:
        m.totProd[t, s] - m.tenderProd[t, s] == m.aboveProd[t, s])

    # Total production
    m.production = pyo.Constraint(
        Ts, S, rule=lambda m, t, s:
        m.solarP[t, s] + m.windP[t, s] + m.coalP[t, s] + m.batteryP[t, s] == m.totProd[t, s])

    # COMPLIANCE CRITERIA

    # Each year
    # Renewable share of production
    m.yearly_renewableShare = pyo.ConstraintList()
    for s in S:
        for year in Years:
            m.yearly_renewableShare.add(
                pyo.quicksum(m.solarP[t, s] + m.windP[t, s] + m.batteryP[t, s] for t in Hours_in_year[year])
                >= pyo.quicksum(m.totProd[t, s] for t in Hours_in_year[year]) * renew_share - m.e_renew_share[year, s])

    # Demand of the tender
    m.yearly_notMetTender = pyo.ConstraintList()
    for s in S:
        for year in Years:
            m.yearly_notMetTender.add(
                pyo.quicksum(m.tenderProd[t, s] for t in Hours_in_year[year])
                >= util_yearly * tau * len(Hours_in_year[year]) - m.e_nonDel_yearly[year, s])

    return m


m = Stochastic()
solver_parameters = "ResultFile=model.ilp"
results = pyo.SolverFactory('gurobi').solve(m, options_string=solver_parameters).write()

########################################################################################################################
# Calculation of LCOE
LCOE_by_scenario = {s: (m.Capex.value + sum(((m.OpexFix[year].value + m.OpexVar[year, s].value
                                              + m.Prod[year, s].value) / pow((1 + r), Y[year])) for year in Years)) /
                       sum(sum(m.totProd[t, s].value for t in Hours_in_year[year]) for year in Years) for s in S}

mean_LCOE = sum(Prob[s] * LCOE_by_scenario[s] for s in S)

########################################################################################################################
# Output
print('\nObjective value')
print(m.NPV())

print('\nCapex')
print(m.Capex.value)
print('\nLCOE_by_scenario')
print({s: LCOE_by_scenario[s] for s in S})
print('\nmean LCOE')
print(mean_LCOE)

print('\nCapacity sizing')
print('\nSolar capacity')
print(m.solarPmax.value)
print('\nWind capacity')
print(m.windPmax.value)
print('\nCoal capacity')
print(m.coalPmax.value)
print('\nBattery power capacity')
print(m.batteryPmax.value)
print('\nBattery energy capacity')
print(m.Emax.value)
print('\nTonnes of CO2 emissions')
print({s: sum(m.CO2Emis[t, s].value for t in Ts) for s in S})

results_hourly = pd.DataFrame()
results_hourly['solar'] = pd.Series({(s, t): m.solarP[t, s].value for t in Ts for s in S})
results_hourly['wind'] = pd.Series({(s, t): m.windP[t, s].value for t in Ts for s in S})
results_hourly['coal'] = pd.Series({(s, t): m.coalP[t, s].value for t in Ts for s in S})
results_hourly['battery'] = pd.Series({(s, t): m.batteryP[t, s].value for t in Ts for s in S})
results_hourly['SOC'] = pd.Series({(s, t): m.E[t, s].value for t in Ts for s in S})
results_hourly['charge'] = pd.Series({(s, t): m.chargeP[t, s].value for t in Ts for s in S})
results_hourly['discharge'] = pd.Series({(s, t): m.dischargeP[t, s].value for t in Ts for s in S})
results_hourly['tender'] = pd.Series({(s, t): m.tenderProd[t, s].value for t in Ts for s in S})
results_hourly['above'] = pd.Series({(s, t): m.aboveProd[t, s].value for t in Ts for s in S})
results_hourly['total production'] = pd.Series({(s, t): m.totProd[t, s].value for t in Ts for s in S})
results_hourly['emissions'] = pd.Series({(s, t): m.CO2Emis[t, s].value for t in Ts for s in S})
results_hourly.index.names = ['scenario', 'time']

results_yearly = pd.DataFrame()
results_yearly['Revenue'] = pd.Series({(s, y): m.Revenue[y, s].value for y in Years for s in S})
results_yearly['ProdCost'] = pd.Series({(s, y): m.Prod[y, s].value for y in Years for s in S})
results_yearly['Penalty'] = pd.Series({(s, y): m.Penalty[y, s].value for y in Years for s in S})
results_yearly['Util penalty'] = pd.Series({(s, y): penalty_utilization_yearly_dyn[y] * m.e_nonDel_yearly[y, s].value
                                            for y in Years for s in S})
results_yearly['Renew penalty'] = pd.Series({(s, y): penalty_renewable_dyn[y] * m.e_renew_share[y, s].value
                                             for y in Years for s in S})
results_yearly['OpexFix'] = pd.Series({(s, y): m.OpexFix[y].value for y in Years for s in S})
results_yearly['OpexVar'] = pd.Series({(s, y): m.OpexVar[y, s].value for y in Years for s in S})
results_yearly['CO2'] = pd.Series({(s, y): sum(m.CO2Emis[t, s].value for t in Hours_in_year[y])
                                   for y in Years for s in S})
results_yearly['total production'] = pd.Series({(s, y): sum(m.totProd[t, s].value for t in Hours_in_year[y])
                                                for y in Years for s in S})
results_yearly['renewable requirement'] = pd.Series({(s, y): renew_share * sum(m.totProd[t, s].value
                                                                               for t in Hours_in_year[y])
                                                     for y in Years for s in S})
results_yearly['yearly R share'] = pd.Series({(s, y): (renew_share * sum(m.totProd[t, s].value
                                                                         for t in Hours_in_year[y])
                                                       - m.e_renew_share[y, s].value) for y in Years for s in S})
results_yearly['tender prod'] = pd.Series({(s, y): sum(m.tenderProd[t, s].value for t in Hours_in_year[y])
                                           for y in Years for s in S})
results_yearly['tender requirement'] = pd.Series({(s, y): util_yearly * tau * len(Hours_in_year[y])
                                                  for y in Years for s in S})
results_yearly['nonDelivered'] = pd.Series({(s, y): m.e_nonDel_yearly[y, s].value for y in Years for s in S})
results_yearly['PPA revenue'] = pd.Series({(s, y): sum(PPA_dyn[y] * m.tenderProd[t, s].value
                                                       for t in Hours_in_year[y]) for y in Years for s in S})
results_yearly['market revenue'] = pd.Series({(s, y): sum(prices[t-1] * m.aboveProd[t, s].value
                                                          for t in Hours_in_year[y]) for y in Years for s in S})
results_yearly['Present value'] = pd.Series({(s, y): m.present_value[y, s].value for y in Years for s in S})
results_yearly['Free Cash Flow'] = pd.Series({(s, y): m.free_cash_flow[y, s].value for y in Years for s in S})
results_yearly.index.names = ['scenario', 'time']

optimal_capacities = pd.Series({'Solar capacity': m.solarPmax.value,
                                'Wind capacity': m.windPmax.value,
                                'Coal capacity': m.coalPmax.value,
                                'Battery power capacity': m.batteryPmax.value,
                                'Battery energy capacity': m.Emax.value,
                                'LCOE': mean_LCOE,
                                'Capex': m.Capex.value,
                                'NPV': m.NPV()})

results_scenario = pd.DataFrame.from_dict({s: {'LCOE': LCOE_by_scenario[s],
                                               'Emissions': sum(m.CO2Emis[t, s].value for t in Ts),
                                               'Scenario years': years_In_Scenario[s]}
                                           for s in S}).T

file1 = results_hourly.to_csv('Results_HPC/Results_Stochastic_hourly_HPC.csv', index=True, header=True)
file2 = results_yearly.to_csv('Results_HPC/Results_Stochastic_yearly_HPC.csv', index=True, header=True)
file3 = optimal_capacities.to_csv('Results_HPC/Results_Stochastic_capacities_HPC.csv', index=True, header=True)
file4 = results_scenario.to_csv('Results_HPC/Results_Stochastic_scenario_HPC.csv', index=True, header=True)






