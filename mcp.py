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

        # collect todays date
        date_today = str(datetime.today()).split()[0]

        # set todays and yesterdays date
        self.tDate = date_today
        self.yDate = date_today.replace(date_today[-1], str(int(date_today[-1]) - 1), -1)

        # yfinance data setup 
        tick = yf.Ticker(ticker)
        self.maturity = tick.options

        # set spot price
        self.spotPrice = tick.info["previousClose"]

        # collect all option data 
        call_data = pd.DataFrame()
        put_data = pd.DataFrame()
        for i in self.maturity:
            option = tick.option_chain(i)
            call_single = pd.concat([pd.DataFrame(), option.calls])
            put_single = pd.concat([pd.DataFrame(), option.puts])
            call_single["maturity"] = i
            put_single["maturity"] = i
            call_data = pd.concat([call_data, call_single], ignore_index=True)
            put_data = pd.concat([put_data, put_single], ignore_index=True)

        # set raw option data
        self.rawData = pd.concat([call_data, put_data], ignore_index=True)

        # clean call data
        # drop unwanted columns
        call_data = call_data.drop(columns=["change", "percentChange", "inTheMoney", "contractSize", "currency", "impliedVolatility"])
        # remove iliquid options, note: regular contracts have a size of 100
        call_data = call_data[call_data["openInterest"] > 50]
        call_data = call_data[call_data["volume"] > 50]
        # set lastTradeDate and maturity from datetime.datetime to datetime.date
        call_data["maturity"] = pd.to_datetime(call_data["maturity"]).dt.date
        call_data["lastTradeDate"] = pd.to_datetime(call_data["lastTradeDate"]).dt.date
        # remove all last traded dates that are not yesterday
        call_data = call_data[call_data["lastTradeDate"] == datetime.strptime(self.yDate, "%Y-%m-%d").date()]
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
        put_data["maturity"] = pd.to_datetime(put_data["maturity"]).dt.date
        put_data["lastTradeDate"] = pd.to_datetime(call_data["lastTradeDate"]).dt.date
        # remove all last traded dates that are not yesterday
        put_data = put_data[put_data["lastTradeDate"] == datetime.strptime(self.yDate, "%Y-%m-%d").date()]
        # drop openIntrest and volume
        put_data = put_data.drop(columns=["openInterest", "volume"])
        # reset index
        put_data = put_data.reset_index(drop=True)

        # set put and call data
        self.callData = call_data
        self.putData = put_data

        # set price matrix
        self.callPriceMatrix = call_data.pivot_table(index="maturity", columns="strike", values="lastPrice")
        self.putPriceMatrix = put_data.pivot_table(index="maturity", columns="strike", values="lastPrice")

## Model and Calibration Class

#SPY = data("SPY")

#print(SPY.putPriceMatrix)

## run/test code

SPY = data("SPY")
print("yes")
