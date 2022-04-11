import numpy as np
from random import choice

Nyears = 30
Nscenarios = 10
from clean_data_NEW import get_clean_data
all_data, Ts, Y, Yp, Years, Hours_in_year = get_clean_data(Nyears)

def Parameters(Nyears, PPA_init = 70, penalty_share_util = 4, penalty_share_ren = 4):

    Wind = all_data['Wind']
    PV = all_data['PV']
    MarketPrices = all_data['2019 euro']
    coalPrice = all_data['Coal price']

    # Capacity factors
    sun = PV / 1000
    CFsolar = sun.to_numpy().flatten()
    CFsolar = np.where(CFsolar>0, CFsolar, 0.0000000000000001)

    wind = Wind / 3300
    CFwind = wind.to_numpy().flatten()
    CFwind = np.where(CFwind>0, CFwind, 0.0000000000000001)

    # Electricity market prices €/MWh
    prices = MarketPrices.to_numpy().flatten() # 0-indexed

    # Coal fuel cost
    coalFuelC = coalPrice.to_numpy().flatten()

    # PPA €/MWh - 25 years of tender
    PPA = PPA_init
    penalty_utilization_yearly = PPA * penalty_share_util
    penalty_renewable = PPA * penalty_share_ren

    PPA_growth = 0.03
    PPA_development = []  # 0-indexed
    for year in Years:
        if year == 'y1':
            PPA_development.append(PPA_init)
        elif year in ['y16', 'y17', 'y18', 'y19', 'y20', 'y21', 'y22', 'y23', 'y24', 'y25']:
            PPA_development.append(PPA_development[Yp[year] - 1] * 1)
        elif year == 'y26':
            PPA_development.append(PPA_development[Yp[year] - 1] * 0)
        else:
            PPA_development.append(PPA_development[Yp[year] - 1] * (1 + PPA_growth))

    PPA_dyn = {y: PPA_development[Yp[y]] for y in Years}
    penalty_utilization_yearly_dyn = {y: penalty_share_util * PPA_dyn[y] for y in Years}
    penalty_renewable_dyn = {y: penalty_share_ren * PPA_dyn[y] for y in Years}

    # Tender demand
    tau = 250

    # Coal online rate
    Cmin = 0.4

    # Battery parameters
    eta_round = 0.8821
    SoCmin = 0.04
    SoCmax = 0.9
    cycles = 365 # per year
    deg = 0.02 # degradation each year
    deg_per_hour = deg / 8760 #len(Hours_in_year[year])
    init = 0.5

    # CO2 emissions, ton/MWh
    coalCO2Emis = 0.98 

    # Thermal efficiency coal
    eta_fuel = 0.44

    # Operational/production cost €/MWh
    solarC = 0
    windC = 0
    coalEmisC = 0
    chargeC = 0

    # Opex variable €/MWh
    solarOpexVar = 0
    windOpexVar = 0
    coalOpexVar = 4.45295
    batteryOpexVar = 0

    # Opex fixed €/MWyr
    solarOpexFix = {y: 12468.26 for y in Years}
    windOpexFix = {y: 39185.96 for y in Years}
    coalOpexFix = {y: 29389.47 for y in Years}
    batteryOpexFix = {y: 31749.5335 for y in Years}
    EOpexFix = {y: 0 for y in Years}

    LT = 30

    # Capex €/MW
    solarCapex = 993007.85*Nyears/LT
    windCapex = 1445427.57*Nyears/LT
    coalCapex = 3528517.58*Nyears/LT
    batteryCapex = 1269981.34*Nyears/LT
    BOS = 594914.12*Nyears/LT # Balance of System/plant
    ECapex = 169212.1*Nyears/LT # Battery pack €/MWh

    # Additional opex for battery for refurbishing the lifetime contract
    # Include at year 11 as battery warranty is 10 years and it can be refurbished once
    refurbish_share = 0.3
    refurbish_bat = refurbish_share * (batteryCapex + BOS)
    refurbish_E = refurbish_share * ECapex
    # later make loop and for 30 years of plant lifetime
    opex_refurbish_bat = {"y1": 0, "y2": 0, "y3": 0, "y4": 0, "y5": 0, "y6": 0, "y7": 0, "y8": 0, "y9": 0, "y10": 0,
                          "y11": refurbish_bat, "y12": 0, "y13": 0, "y14": 0, "y15": 0, "y16": 0, "y17": 0, "y18": 0,
                          "y19": 0, "y20": 0, "y21": refurbish_bat, "y22": 0, "y23": 0, "y24": 0, "y25": 0, "y26": 0,
                          "y27": 0, "y28": 0, "y29": 0, "y30": 0}
    opex_refurbish_E = {"y1": 0, "y2": 0, "y3": 0, "y4": 0, "y5": 0, "y6": 0, "y7": 0, "y8": 0, "y9": 0, "y10": 0,
                        "y11": refurbish_E, "y12": 0, "y13": 0, "y14": 0, "y15": 0, "y16": 0, "y17": 0, "y18": 0,
                        "y19": 0, "y20": 0, "y21": refurbish_E, "y22": 0, "y23": 0, "y24": 0, "y25": 0, "y26": 0,
                        "y27": 0, "y28": 0, "y29": 0, "y30": 0}

    # Grid-constrained capacity
    GC = 500

    # Discount rate India
    r = 0.11

    # Compliance
    # Utilisation efficiency
    util_yearly = 0.85
    # Renewable share
    renew_share = 0.51

    return CFsolar, CFwind, prices, tau, PPA, penalty_utilization_yearly, penalty_renewable,\
           Cmin, eta_round, SoCmin, SoCmax, cycles, deg_per_hour, coalCO2Emis, eta_fuel, solarC, windC, coalFuelC, \
           chargeC, solarOpexVar, windOpexVar, coalOpexVar, coalEmisC, batteryOpexVar, solarOpexFix, windOpexFix, \
           coalOpexFix, batteryOpexFix, EOpexFix, solarCapex, windCapex, coalCapex, batteryCapex, BOS, ECapex, GC, r, \
           util_yearly, renew_share, PPA_dyn, penalty_utilization_yearly_dyn, penalty_renewable_dyn, \
           opex_refurbish_bat, opex_refurbish_E, init


def Scenarios(Nscenarios):
    S = [f"s{i + 1}" for i in range(Nscenarios)]
    Prob = {s: (1/len(S)) for s in S}
    return S, Prob

def ShuffleCFs(CFwind, CFsolar, prices, coalFuelC, Nyears, local_Hours_in_year=Hours_in_year):
    newCFwind = []
    newCFsolar = []
    shuffleYears = []
    newPrices = []
    newCoalFuelC = []
    years = list(local_Hours_in_year.keys())
    for y in range(Nyears):
        year = choice(years)
        newCFwind.append(CFwind[local_Hours_in_year[year]])
        newCFsolar.append(CFsolar[local_Hours_in_year[year]])
        shuffleYears.append(year)
        newPrices.append(prices[local_Hours_in_year[year]])
        newCoalFuelC.append(coalFuelC[local_Hours_in_year[year]])
    newCFwind = np.concatenate(newCFwind)
    newCFsolar = np.concatenate(newCFsolar)
    newPrices = np.concatenate(newPrices)
    newCoalFuelC = np.concatenate(newCoalFuelC)
    return newCFwind, newCFsolar, shuffleYears, newPrices, newCoalFuelC









