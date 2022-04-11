import pyomo.environ as pyo
from itertools import islice
import pandas as pd

def function1(tau_s = 250, renew_max = 300, coal_max = 250, battery_max = 250,
              energy_max = 300):
    Nyears = 1
    from clean_data_NEW import get_clean_data
    all_data, Ts, Y, Yp, Years, Hours_in_year = get_clean_data(Nyears)
    from parameters_NEW import Parameters
    CFsolar, CFwind, prices, tau, PPA, penalty_utilization_yearly, penalty_renewable, \
    Cmin, eta_round, SoCmin, SoCmax, cycles, deg_per_hour, coalCO2Emis, eta_fuel, solarC, windC, coalFuelC, \
    chargeC, solarOpexVar, windOpexVar, coalOpexVar, coalEmisC, batteryOpexVar, solarOpexFix, windOpexFix, \
    coalOpexFix, batteryOpexFix, EOpexFix, solarCapex, windCapex, coalCapex, batteryCapex, BOS, ECapex, GC, r, \
    util_yearly, renew_share, PPA_dyn, penalty_utilization_yearly_dyn, penalty_renewable_dyn, \
    opex_refurbish_bat, opex_refurbish_E, init = Parameters(Nyears)
    ####################################################################################################################

    def Economic_dispatch(tau_s = 250, renew_max = 300, coal_max = 250, battery_max = 250, energy_max = 300):
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
        m.e_nonDel_yearly = pyo.Var(Years, domain=pyo.NonNegativeReals)

        m.prods = pyo.Var(Ts, domain=pyo.NonNegativeReals)
        m.Prod = pyo.Var(Years, domain=pyo.NonNegativeReals)
        m.revs = pyo.Var(Ts, domain=pyo.Reals)
        m.Revenue = pyo.Var(Years, domain=pyo.Reals)
        m.Penalty = pyo.Var(Years, domain=pyo.Reals)

        # Objective
        m.cost = pyo.Objective(expr=sum(m.Prod[year] - m.Revenue[year] + m.Penalty[year] for year in Years),
                               sense=pyo.minimize)

        m.P = pyo.Constraint(
            Ts, rule=lambda m, t:
            solarC * m.solarP[t]
            + windC * m.windP[t]
            + (coalFuelC[t-1] / eta_fuel) * m.coalP[t]
            + chargeC * m.batteryP[t]
            == m.prods[t])

        m.PROD = pyo.ConstraintList()
        for year in Years:
            m.PROD.add(pyo.quicksum(m.prods[t] for t in Hours_in_year[year]) <= m.Prod[year])

        m.R = pyo.Constraint(
            Ts, rule=lambda m, t:
            prices[t-1] * m.aboveProd[t]
            + PPA * m.tenderProd[t]
            == m.revs[t])

        m.REVENUE = pyo.ConstraintList()
        for year in Years:
            m.REVENUE.add(pyo.quicksum(m.revs[t] for t in Hours_in_year[year]) >= m.Revenue[year])

        m.PENALTY = pyo.Constraint(
            Years, rule=lambda m, year:
            penalty_utilization_yearly * m.e_nonDel_yearly[year] <= m.Penalty[year])

        # Renewable production capacity
        m.PV = pyo.Constraint(Ts, rule=lambda m, t: m.solarP[t] <= float(CFsolar[t-1]) * renew_max)
        m.Turbine = pyo.Constraint(Ts, rule=lambda m, t: m.windP[t] <= float(CFwind[t-1]) * renew_max)

        # Coal has to stay on-line all the time due to technical limitations
        m.coalOnline = pyo.Constraint(Ts, rule=lambda m, t: m.coalP[t] >= Cmin * coal_max)
        m.coalMax = pyo.Constraint(Ts, rule=lambda m, t: m.coalP[t] <= coal_max)

        # Battery production
        m.batMin = pyo.Constraint(Ts, rule=lambda m, t: m.batteryP[t] >= -battery_max)
        m.batMax = pyo.Constraint(Ts, rule=lambda m, t: m.batteryP[t] <= battery_max)
        m.batCharge = pyo.Constraint(Ts, rule=lambda m, t: m.chargeP[t] <= battery_max)
        m.batDischarge = pyo.Constraint(Ts, rule=lambda m, t: m.dischargeP[t] <= battery_max)
        m.bat = pyo.Constraint(Ts, rule=lambda m, t: m.batteryP[t] == m.dischargeP[t] - m.chargeP[t])

        # Limit the use of battery cycles to 365 each year
        m.cycleLife = pyo.ConstraintList()
        for year in Years:
            m.cycleLife.add(pyo.quicksum(m.dischargeP[t] for t in Hours_in_year[year]) <= cycles * battery_max)

        # Battery is charged by renewable power
        m.batRenewable = pyo.Constraint(Ts, rule=lambda m, t: m.chargeP[t] <= m.solarP[t] + m.windP[t])

        # State of Charge - battery energy
        m.SoC_lower = pyo.Constraint(Ts, rule=lambda m, t: m.E[t] >= SoCmin * energy_max)
        m.SoC_upper = pyo.Constraint(Ts, rule=lambda m, t: m.E[t] <= SoCmax * energy_max)
        m.EnergyZero = pyo.Constraint(rule=lambda m: m.E[Ts[0]] == init * energy_max)
        m.Energy = pyo.ConstraintList()
        for t, tneg1 in zip(islice(Ts, 1, None), Ts):
            m.Energy.add(m.E[t] == m.E[tneg1] + eta_round * m.chargeP[t] - m.dischargeP[t])

        # Total production
        m.production = pyo.Constraint(
            Ts, rule=lambda m, t: m.solarP[t] + m.windP[t] + m.coalP[t] + m.batteryP[t] == m.totProd[t])

        # Tender production and above
        m.deliverTender = pyo.Constraint(Ts, rule=lambda m, t: m.tenderProd[t] <= tau_s)
        m.limitTender = pyo.Constraint(Ts, rule=lambda m, t: m.tenderProd[t] <= m.totProd[t])
        m.aboveTender = pyo.Constraint(Ts, rule=lambda m, t: m.totProd[t] - m.tenderProd[t] == m.aboveProd[t])

        # Tender not met - sliding production level with penalty for not meeting demand
        m.yearly_notMetTender = pyo.ConstraintList()
        for year in Years:
            m.yearly_notMetTender.add(
                pyo.quicksum(m.tenderProd[t] for t in Hours_in_year[year])
                >= tau_s * len(Hours_in_year[year]) - m.e_nonDel_yearly[year])

        return m

    m = Economic_dispatch(tau_s=tau_s, renew_max=renew_max, coal_max=coal_max,
                          battery_max=battery_max, energy_max=energy_max)
    solver_parameters = "ResultFile=model.ilp"
    results = pyo.SolverFactory('gurobi').solve(m, options_string=solver_parameters).write()

    ####################################################################################################################
    # Output
    print('\nObjective value')
    print(m.cost())

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
                                                 'prod': m.prods[t].value,
                                                 'revenue': m.revs[t].value}
                                             for t in Ts}).T

    results_yearly = pd.DataFrame.from_dict({y: {'nonDel_yearly': m.e_nonDel_yearly[y].value,
                                                 'ProdCost': m.Prod[y].value,
                                                 'Revenue': m.Revenue[y].value,
                                                 'Penalty': m.Penalty[y].value}
                                             for y in Years}).T

    objective = pd.Series({'objective value': m.cost()})
    return results_hourly, results_yearly, objective




