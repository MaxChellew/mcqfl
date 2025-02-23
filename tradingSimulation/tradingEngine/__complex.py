#######################################################

# Author: Max Chellew
# Libary: emarci

#######################################################

# Global Libary imports: numpy, pandas
import numpy as np 
import sympy as sp 
import pandas as pd 

# Local Libary imports: NaN

#######################################################

def checkLimitOrders():
    pass

def checkStopOrders():
    pass

def checkLimitStopOrders():
    pass

#######################################################

# Class: engineSimple
class complex:
    """
    Inputs:
    - stock_data (pandas DataFrame) | index > "Date", Columns > "price" "
    - commission_fee (int) | 

    Output: 

    """

    # function: __init__
    def __init__(self, price_data, commission_rate, initial_balance):
        pass

    # function: executeMarketOrder
    def executeMarketOrder(self, ticker, action, trade_volume, date):
        pass
    
    # function: executeLimitOrder
    def executeLimitOrder(self, ticker, action, trade_volume, limit_price, date):
        pass 
    
    # function: executeStopOrder
    def executeStopOrder(self, ticker, action, trade_volume, stop_price, date):
        pass 

    # function: executeStopLimitOrder
    def executeStopLimitOrder(self, ticker, action, trade_volume, stop_price, limit_price, date):
        pass 
    
    # function: executedInstructedOrder
    def executeIntstuctedOrder(self, ticker, action, trade_volume, stop_loss, stop_profit, date):
        pass

        