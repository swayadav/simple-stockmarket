import pandas as pd
import numpy as np
from pytz import timezone 
from datetime import datetime
import pandasql as psql

india_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')

stock_data = pd.read_csv('stock_data.csv')
print(stock_data)
stock_data['Fixed Dividend'] = stock_data['Fixed Dividend'].replace(np.nan, 0)


def dividend_yeild(stock_sym, price):
    stock_sym_df = stock_data[stock_data['Stock Symbol'].isin([stock_sym])]
    print(stock_sym_df)
    common_or_preferred = stock_sym_df['Type'].tolist()[0]
    print(common_or_preferred)
    print(type(common_or_preferred))

    if common_or_preferred == "Common":
        operation_result = (stock_sym_df['Last Dividend'].tolist()[0]//int(price))
    else:
        operation_result = (((int(stock_sym_df['Fixed Dividend'].tolist()[0][0]*100))*int(stock_sym_df['Par Value'].tolist()[0]))//int(price))
        print(operation_result)
    return '{:.1%}'.format(round(operation_result))


def pe_ratio(stock_sym, price):
    stock_sym_df = stock_data[stock_data['Stock Symbol'].isin([stock_sym])]
    print(stock_sym_df)
    last_dividend = stock_sym_df['Last Dividend'].tolist()[0]
    print(last_dividend)
    operation_result = (int(price)//int(last_dividend))
    print(operation_result)
    return '{:.1%}'.format(operation_result)


def trade(stock_sym, price, buy_sell):
    holding_shares = 1000 
    stock_sym_df = stock_data[stock_data['Stock Symbol'].isin([stock_sym])]
    par_value = stock_sym_df['Par Value'].tolist()[0]
    if buy_sell == "BUY":
        no_of_shares_purchased = (int(price)//int(par_value))
        operation_result = "{} Trade has been executed for {} : {} Shares of Value {} purchased at {} IST".format(buy_sell, stock_sym, no_of_shares_purchased, price, india_time)
    else:
        operation_result = "{} Trade has been executed for {} : {} Shares of Value {} Sold at {} IST".format(buy_sell, stock_sym, 22, 2200, india_time)
    
    return operation_result


def calculate_vwsp():
    operation_result = "sdsad"
    return operation_result


def calculate_gbce():
    operation_result = "sdsad"
    return operation_result



    














