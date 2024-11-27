### BlackScholes Libary

# Author: Max Chellew

## Libarys

# Import Global Libarys
import numpy as np
import scipy as sp
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

# Import Local Libary
import BlackScholes as bs

## Data Class

# Create data class
class data:

    def __init__(self, ticker):
        
        # set ticker
        self.ticker = ticker

        # set todays date
        self.date = str(datetime.today()).split()[0]

        # yfinance data setup 
        tick = yf.Ticker(ticker)
        self.maturity = tick.options

        # collect all option data 
        call_data = pd.DataFrame()
        put_data = pd.DataFrame()
        for i in self.maturity:
            option = tick.option_chain(i)
            call_single = pd.concat([pd.DataFrame(), option.calls])
            put_single = pd.concat([pd.DataFrame(), option.puts])
            call_single["matuirty"] = i
            put_single["matuirty"] = i
            call_data = pd.concat([call_data, call_single], ignore_index=True)
            put_data = pd.concat([put_data, put_single], ignore_index=True)

        # set raw option data
        self.raw_data = pd.concat([call_data, put_data], ignore_index=True)

        # clean call data
        # drop unwanted columns
        call_data = call_data.drop(columns=["change", "percentChange", "inTheMoney", "contractSize", "currency", "impliedVolatility"])
        # remove iliquid options, note: regular contracts have a size of 100
        call_data = call_data[call_data["openInterest"] > 50]
        call_data = call_data[call_data["volume"] > 50]
        # set lastTradeDate and matuirty from datetime.datetime to datetime.date
        call_data["matuirty"] = pd.to_datetime(call_data["matuirty"]).dt.date
        call_data["lastTradeDate"] = pd.to_datetime(call_data["lastTradeDate"]).dt.date
        # remove all last traded dates that are not yesterday
        call_data = call_data[call_data["lastTradeDate"] == datetime.strptime(self.date, "%Y-%m-%d").date()]
        # drop openIntrest and volume
        call_data = call_data.drop(columns=["openInterest", "volume"])
        # reset index
        call_data = call_data.reset_index(drop=True)

        # clean put data
        # drop unwanted columns
        put_data = put_data.drop(columns=["change", "percentChange", "inTheMoney", "contractSize", "currency", "impliedVolatility"])
        # remove iliquid options, note: regular contracts have a size of 100
        put_data = put_data[put_data["openInterest"] > 50]
        put_data = put_data[put_data["volume"] > 50]
        # set lastTradeDate from datetime.datetime to datetime.date
        put_data["matuirty"] = pd.to_datetime(put_data["matuirty"]).dt.date
        put_data["lastTradeDate"] = pd.to_datetime(call_data["lastTradeDate"]).dt.date
        # remove all last traded dates that are not yesterday
        put_data = put_data[put_data["lastTradeDate"] == datetime.strptime(self.date, "%Y-%m-%d").date()]
        # drop openIntrest and volume
        put_data = put_data.drop(columns=["openInterest", "volume"])
        # reset index
        put_data = put_data.reset_index(drop=True)

        # set put and call data
        self.call_data = call_data
        self.put_data = put_data



yes = data("SPY")
no = yes.call_data
print(no)

## Model and Calibration Class