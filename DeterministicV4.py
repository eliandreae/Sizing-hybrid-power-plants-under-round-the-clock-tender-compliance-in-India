import pyomo.environ as pyo
from itertools import islice
import pandas as pd

Nyears = 30
from clean_data_NEW import get_clean_data
all_data, Ts, Y, Yp, Years, Hours_in_year = get_clean_data(Nyears)
from parameters_NEW import Parameters
CFsolar, CFwind, prices, tau, PPA, penalty_utilization_yearly, penalty_renewable,\
           Cmin, eta_round, SoCmin, SoCmax, cycles, deg_per_hour, coalCO2Emis, eta_fuel, solarC, windC, coalFuelC, \
           chargeC, solarOpexVar, windOpexVar, coalOpexVar, coalEmisC, batteryOpexVar, solarOpexFix, windOpexFix, \
           coalOpexFix, batteryOpexFix, EOpexFix, solarCapex, windCapex, coalCapex, batteryCapex, BOS, ECapex, GC, r, \
           util_yearly, renew_share, PPA_dyn, penalty_utilization_yearly_dyn, penalty_renewable_dyn, \
           opex_refurbish_bat, opex_refurbish_E, init = Parameters(Nyears)

########################################################################################################################

def Deterministic():
    m = pyo.ConcreteModel()

    m.solarP = pyo.Var(Ts, domain=pyo.NonNegativeReals)
    m.windP = pyo.Var(Ts, domain=pyo.NonNegativeReals)
    m.coalP = pyo.Var(Ts, domain=pyo.NonNegativeReals)
    m.batteryP = pyo.Var(Ts, domain=pyo.Reals)
    m.chargeP = pyo.Var(Ts, domain=pyo.NonNegativeReals)
    m.dischargeP = pyo.Var(Ts, domain=pyo.NonNegativeReals)
    m.E = pyo.Var(Ts, domain=pyo.Reals)

    m.totProd = pyo.Var(Ts, domain=pyo.NonNegativeReals)
    m.tenderProd = pyo.Var(Ts, domain=pyo.NonNegativeReals)
    m.aboveProd = pyo.Var(Ts, domain=pyo.NonNegativeReals)

    m.CO2Emis = pyo.Var(Ts, domain=pyo.NonNegativeReals)

    m.e_nonDel_yearly = pyo.Var(Years, domain=pyo.NonNegativeReals)
    m.e_renew_share = pyo.Var(Years, domain=pyo.NonNegativeReals)

    m.solarPmax = pyo.Var(domain=pyo.NonNegativeReals)
    m.windPmax = pyo.Var(domain=pyo.NonNegativeReals)
    m.coalPmax = pyo.Var(domain=pyo.NonNegativeReals, bounds=(0, tau))
    m.batteryPmax = pyo.Var(domain=pyo.NonNegativeReals, bounds=(0, tau))
    m.Emax = pyo.Var(domain=pyo.NonNegativeReals)

    m.Capex = pyo.Var(domain=pyo.NonNegativeReals)
    m.OpexFix = pyo.Var(Years, domain=pyo.NonNegativeReals)
    m.OpexVar = pyo.Var(Years, domain=pyo.NonNegativeReals)
    m.Prod = pyo.Var(Years, domain=pyo.NonNegativeReals)
    m.Revenue = pyo.Var(Years, domain=pyo.Reals)
    m.Penalty = pyo.Var(Years, domain=pyo.Reals)

    m.present_value = pyo.Var(Years, domain=pyo.Reals)
    m.free_cash_flow = pyo.Var(Years, domain=pyo.Reals)

    # Objective - Maximise NPV
    m.NPV = pyo.Objective(expr=sum((1/pow((1 + r), Y[year])) * (m.Revenue[year] - m.Prod[year] - m.OpexVar[year]
                          - m.OpexFix[year] - m.Penalty[year]) for year in Years) - m.Capex
                          , sense=pyo.maximize)

    m.PresentValue = pyo.ConstraintList()
    for year in Years:
        m.PresentValue.add((1/pow((1 + r), Y[year])) * (m.Revenue[year] - m.Prod[year] - m.OpexVar[year]
                                                        - m.OpexFix[year] - m.Penalty[year]) == m.present_value[year])

    m.FreeCashFlow = pyo.ConstraintList()
    for year in Years:
        m.FreeCashFlow.add(m.Revenue[year] - m.Prod[year] - m.OpexVar[year] - m.OpexFix[year] - m.Penalty[year]
                           == m.free_cash_flow[year])

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
    for year in Years:
        m.OPEXvar.add(pyo.quicksum(solarOpexVar * m.solarP[t]
                                   + windOpexVar * m.windP[t]
                                   + coalOpexVar * m.coalP[t]
                                   + batteryOpexVar * m.batteryP[t] for t in Hours_in_year[year])
                      <= m.OpexVar[year])

    m.PROD = pyo.ConstraintList()
    for year in Years:
        m.PROD.add(pyo.quicksum(solarC * m.solarP[t]
                                + windC * m.windP[t]
                                + ((coalFuelC[t - 1] + coalEmisC * coalCO2Emis)/eta_fuel) * m.coalP[t]
                                + chargeC * m.batteryP[t] for t in Hours_in_year[year])
                   <= m.Prod[year])

    m.REVENUE = pyo.ConstraintList()
    for year in Years:
        m.REVENUE.add(pyo.quicksum(prices[t - 1] * m.aboveProd[t]
                                   + PPA_dyn[year] * m.tenderProd[t] for t in Hours_in_year[year])
                      >= m.Revenue[year])

    # Pay the largest penalty
    m.PENALTY1 = pyo.ConstraintList()
    m.PENALTY2 = pyo.ConstraintList()
    for year in Years:
        m.PENALTY1.add(penalty_utilization_yearly_dyn[year] * m.e_nonDel_yearly[year] <= m.Penalty[year])
        m.PENALTY2.add(penalty_renewable_dyn[year] * m.e_renew_share[year] <= m.Penalty[year])

    # Grid-constrained capacity
    m.grid = pyo.Constraint(Ts, rule=lambda m, t: m.solarP[t] + m.windP[t] + m.batteryP[t] <= GC)

    # Renewable production capacity
    m.PV = pyo.Constraint(Ts, rule=lambda m, t: m.solarP[t] <= float(CFsolar[t-1]) * m.solarPmax)
    m.Turbine = pyo.Constraint(Ts, rule=lambda m, t: m.windP[t] <= float(CFwind[t-1]) * m.windPmax)

    # Coal has to stay on-line all the time due to technical limitations
    m.coalOnline = pyo.Constraint(Ts, rule=lambda m, t: m.coalP[t] >= Cmin * m.coalPmax)
    m.coalMax = pyo.Constraint(Ts, rule=lambda m, t: m.coalP[t] <= m.coalPmax)

    # Tons of C02 emissions from coal
    m.Emissions = pyo.Constraint(Ts, rule=lambda m, t: coalCO2Emis * m.coalP[t] == m.CO2Emis[t])

    # Battery production
    m.batMin = pyo.Constraint(Ts, rule=lambda m, t: m.batteryP[t] >= -m.batteryPmax)
    m.batMax = pyo.Constraint(Ts, rule=lambda m, t: m.batteryP[t] <= m.batteryPmax)
    m.batCharge = pyo.Constraint(Ts, rule=lambda m, t: m.chargeP[t] <= m.batteryPmax)
    m.batDischarge = pyo.Constraint(Ts, rule=lambda m, t: m.dischargeP[t] <= m.batteryPmax)
    m.bat = pyo.Constraint(Ts, rule=lambda m, t: m.batteryP[t] == m.dischargeP[t] - m.chargeP[t])

    # Battery is charged by renewable power
    m.batRenewable = pyo.Constraint(Ts, rule=lambda m, t: m.chargeP[t] <= m.solarP[t] + m.windP[t])

    # State of Charge - battery energy
    m.SoC_lower = pyo.Constraint(Ts, rule=lambda m, t: m.E[t] >= SoCmin * m.Emax)
    m.SoC_upper = pyo.Constraint(Ts, rule=lambda m, t: m.E[t] <= SoCmax * m.Emax)
    m.EnergyZero = pyo.Constraint(rule=lambda m: m.E[Ts[0]] == init * m.Emax)
    m.Energy = pyo.ConstraintList()
    for t, tneg1 in zip(islice(Ts, 1, None), Ts):
        m.Energy.add(m.E[t] == m.E[tneg1] + eta_round * m.chargeP[t] - m.dischargeP[t])

    # Battery degradation over years
    m.degradation = pyo.ConstraintList()
    for year in Years:
        for t in Hours_in_year[year]:
            degradationfactor = max(0.9, (1 - deg_per_hour * t))
            m.degradation.add(m.Emax * degradationfactor >= m.E[t])

    # Limit the use of battery cycles to 365 each year
    m.cycleLife = pyo.ConstraintList()
    for year in Years:
        m.cycleLife.add(pyo.quicksum(m.dischargeP[t] for t in Hours_in_year[year]) <= cycles * m.batteryPmax)

    # Tender production and above
    m.deliverTender = pyo.Constraint(Ts, rule=lambda m, t: m.tenderProd[t] <= tau)
    m.limitTender = pyo.Constraint(Ts, rule=lambda m, t: m.tenderProd[t] <= m.totProd[t])
    m.aboveTender = pyo.Constraint(Ts, rule=lambda m, t: m.totProd[t] - m.tenderProd[t] == m.aboveProd[t])

    # Total production
    m.production = pyo.Constraint(
        Ts, rule=lambda m, t:
        m.solarP[t] + m.windP[t] + m.coalP[t] + m.batteryP[t] == m.totProd[t])

    # COMPLIANCE CRITERIA
    # Each year
    # Renewable share of production
    m.yearly_renewableShare = pyo.ConstraintList()
    for year in Years:
        m.yearly_renewableShare.add(
            pyo.quicksum(m.solarP[t] + m.windP[t] + m.batteryP[t] for t in Hours_in_year[year])
            >= pyo.quicksum(m.totProd[t] for t in Hours_in_year[year]) * renew_share - m.e_renew_share[year])

    # Demand of the tender is average 85% of 250MW hourly production each year (>85% utilisation efficiency each year)
    m.yearly_notMetTender = pyo.ConstraintList()
    for year in Years:
        m.yearly_notMetTender.add(
            pyo.quicksum(m.tenderProd[t] for t in Hours_in_year[year])
            >= util_yearly * tau * len(Hours_in_year[year]) - m.e_nonDel_yearly[year])

    return m


m = Deterministic()
solver_parameters = "ResultFile=model.ilp"
results = pyo.SolverFactory('gurobi').solve(m, options_string=solver_parameters, tee=True,
                                            logfile='what_happens.log').write()

########################################################################################################################
# Calculation of LCOE
LCOE = (m.Capex.value + sum(((m.OpexFix[year].value + m.OpexVar[year].value + m.Prod[year].value)/pow((1 + r), Y[year]))
                            for year in Years)) / sum(sum(m.totProd[t].value for t in Hours_in_year[year])
                                                      for year in Years)

########################################################################################################################
# Output
print('\nObjective value')
print(m.NPV())

print('\nCapex')
print(m.Capex.value)
print('\nLCOE')
print(LCOE)

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
print(sum(m.CO2Emis[t].value for t in Ts))

results_hourly = pd.DataFrame.from_dict({t: {'solar': m.solarP[t].value,
                                             'wind': m.windP[t].value,
                                             'coal': m.coalP[t].value,
                                             'battery': m.batteryP[t].value,
                                             'SoC': m.E[t].value,
                                             'charge': m.chargeP[t].value,
                                             'discharge': m.dischargeP[t].value,
                                             'tender': m.tenderProd[t].value,
                                             'above': m.aboveProd[t].value,
                                             'total production': m.totProd[t].value,
                                             'emissions': m.CO2Emis[t].value}
                                         for t in Ts}).T

results_yearly = pd.DataFrame.from_dict({y: {'ProdCost': m.Prod[y].value,
                                             'Revenue': m.Revenue[y].value,
                                             'Penalty': m.Penalty[y].value,
                                             'Util penalty': penalty_utilization_yearly_dyn[y]
                                                             * m.e_nonDel_yearly[y].value,
                                             'Renew penalty': penalty_renewable_dyn[y] * m.e_renew_share[y].value,
                                             'OpexFix': m.OpexFix[y].value,
                                             'OpexVar': m.OpexVar[y].value,
                                             'CO2': sum(m.CO2Emis[t].value for t in Hours_in_year[y]),
                                             'totProd': sum(m.totProd[t].value for t in Hours_in_year[y]),
                                             'renewable requirement': renew_share * sum(m.totProd[t].value
                                                                                        for t in Hours_in_year[y]),
                                             'yearly R share': renew_share * sum(
                                                     m.totProd[t].value for t in Hours_in_year[y])
                                                                   - m.e_renew_share[y].value,
                                             'tender prod': sum(m.tenderProd[t].value for t in Hours_in_year[y]),
                                             'tender requirement': util_yearly * tau * len(Hours_in_year[y]),
                                             'nonDel_yearly': m.e_nonDel_yearly[y].value,
                                             'market revenue': sum(prices[t - 1] * m.aboveProd[t].value
                                                                       for t in Hours_in_year[y]),
                                             'PPA revenue': sum(PPA_dyn[y] * m.tenderProd[t].value
                                                                for t in Hours_in_year[y]),
                                             'Present value': m.present_value[y].value,
                                             'Free Cash Flow': m.free_cash_flow[y].value}
                                         for y in Years}).T

optimal_capacities = pd.Series({'Solar capacity': m.solarPmax.value,
                                'Wind capacity': m.windPmax.value,
                                'Coal capacity': m.coalPmax.value,
                                'Battery power capacity': m.batteryPmax.value,
                                'Battery energy capacity': m.Emax.value,
                                'LCOE': LCOE,
                                'Capex': m.Capex.value,
                                'NPV': m.NPV()})

file1 = results_hourly.to_csv('Results_HPC/Results_Deterministic_hourly_HPC.csv', index=False, header=True)
file2 = results_yearly.to_csv('Results_HPC/Results_Deterministic_yearly_HPC.csv', index=False, header=True)
file3 = optimal_capacities.to_csv('Results_HPC/Results_Deterministic_capacities_HPC.csv', index=False, header=True)



