import numpy as np
import pandas as pd

Nyears = 30
def get_clean_data(Nyears, future_elec_price_change = None):

    if future_elec_price_change is None:
        future_elec_price_change = 1.0609

    # Segmentation of time
    Years = [f"y{i+1}" for i in range(Nyears)]
    Y = {y: i+1 for i,y in enumerate(Years)}
    Yp = {y: i for i, y in enumerate(Years)}
    Ys = list(range(1,Nyears+1))

    Hours_in_year = {}
    for x in Ys:
        offset = (x - 1) * 8760
        newElementName = 'y' + str(x)
        newElementValue = list(range(offset, offset + 8760))
        Hours_in_year[newElementName] = newElementValue

    Ts = [t for y in Years for t in Hours_in_year[y]]

########################################################################################################################

    # Power data
    data = pd.read_csv("ts_output_clean.csv", skipinitialspace=True, usecols=["timestamp", "PV", "Wind"])

    ####################################################################################################################

    # Electricity prices
    inflation = future_elec_price_change
    merchant_prices = pd.read_excel('merchant_prices.xlsx', sheet_name='2019 euro', header=None, parse_dates=True)
    merchant_prices['timestamp'] = merchant_prices[0].astype(str) + ' ' + merchant_prices[1].astype(str)
    merchant_prices['timestamp'] = pd.to_datetime(merchant_prices['timestamp'].apply(lambda x: f'{x[:-5]}:00:00'))
    merchant_prices.columns = ['year', 'hour', '2019 euro', 'timestamp']
    merchant_prices.drop_duplicates(subset=['timestamp'], keep='first', inplace=True)

    el_prices = merchant_prices.copy()
    merchant_prices['inf euro'] = el_prices['2019 euro'].apply(lambda x: x * pow(inflation, 18))
    for idx, year in enumerate(Years):
        temp = el_prices.copy()
        if year == 'y19':
            continue

        temp['timestamp'] = temp['timestamp'].add(pd.offsets.DateOffset(years=idx-19))
        temp['inf euro'] = temp['2019 euro'].apply(lambda x: x * pow(inflation, idx))
        merchant_prices = merchant_prices.append(temp)

    merchant_prices.drop_duplicates(subset=['timestamp'], keep='first', inplace=True)
    merchant_prices['timestamp'] = pd.to_datetime(merchant_prices['timestamp'])
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    all_data = data.merge(merchant_prices, how='left', on='timestamp')
    all_data.sort_values('timestamp', inplace=True)
    all_data['2019 euro'].fillna(value=all_data['2019 euro'].mean(), inplace=True)
    all_data['inf euro'].fillna(value=all_data['inf euro'].mean(), inplace=True)
    # Null values in wind column to 0.0
    all_data['Wind'].fillna(value=0.0, inplace=True)

    ####################################################################################################################

    # Coal prices
    coal_prices = pd.read_excel('coal_prices.xlsx', sheet_name='price')
    all_data['id'] = all_data.apply(lambda row: str(row['timestamp'].year) + '_' +
                                                str(row['timestamp'].month), axis=1)
    all_data = all_data.merge(coal_prices, how='left', on='id')
    all_data = all_data[all_data['timestamp'] < '2042-01-01 00:00:00']

    return all_data, Ts, Y, Yp, Years, Hours_in_year
########################################################################################################################

if __name__ == '__main__':
    for output in get_clean_data(Nyears):
        print()






























