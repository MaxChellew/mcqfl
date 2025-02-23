#######################################################

# Author: Max Chellew
# Libary: emarci

#######################################################

# Global Libary imports: numpy, pandas
import numpy as np
import pandas as pd 

# Local Libary imports: NaN

#######################################################

class engineSimple:
    """
    Inputs:
    "insert text here"

    Output: 
    "insert text here"
    """

    #######################################################
    ## initalise Functions

    # function: __init__
    def __init__(self, price_data, commission_rate, initial_balance):
    
        # set self.X (Variables Fixed)
        self.price_data = price_data
        self.commission_rate = commission_rate

        # set self.X (variables Non-fixed)
        self.total_commission_costs = 0
        self.balance = initial_balance
        self.PnL = 0
        self.PnL_without_commisions = 0

        # Create empty pandas DataFrames
        df_trade_positions = pd.DataFrame([[None]*(len(price_data.columns.levels[1].values)*2)],
                                                   index=[0],
                                                   columns= pd.MultiIndex.from_product([["Trade Direction", "Trade Volume"], price_data.columns.levels[1].values], names=['Category', 'Ticker']))
        df_trade_history = pd.DataFrame([[None]*7],
                                                 index=[0],
                                                 columns=["Date", "Ticker", "Action", "Trade Volume", "Price", "Type", "Commission Fee"])

        # set index name of pandas DataFrames 
        df_trade_positions.index.name = "Date"
        df_trade_history.index.name = "Entry"

        # set self.X (pandas DataFrames)
        self.trade_positions = df_trade_positions.drop(0)
        self.trade_history = df_trade_history.drop(0)

    #######################################################
    ## Trading Functions

    # function: executeMarketOrder
    def executeMarketOrder(self, ticker, action, trade_volume, date):

        # trade info
        current_price = self.price_data["Price", ticker].loc[date]
        commission_fee = self.commission_rate * current_price * trade_volume

        # update trade history
        self.trade_history.loc[len(self.trade_history.index)] = [date, ticker, action, trade_volume, current_price, "Market Order", commission_fee]
        
        # update balance
        if action == "BUY":
            self.balance -= current_price * trade_volume - commission_fee
        elif action == "SELL":
            self.balance += current_price * trade_volume - commission_fee

        # update total commission fee
        self.total_commission_costs  = self.trade_history["Commission Fee"].sum()

        # seperate BUY and SELL orders
        buy_orders = self.trade_history[(self.trade_history["Action"] == "BUY").values]
        sell_orders = self.trade_history[(self.trade_history["Action"] == "SELL").values]

        # Calculate Total Trade Volume (List)
        total_trade_volume = (buy_orders.groupby("Ticker")["Trade Volume"].sum()).sub(sell_orders.groupby("Ticker")["Trade Volume"].sum(), fill_value=0).add(pd.Series([0, 0], index=self.price_data.columns.levels[1].values), fill_value=0)
        
        # update Trade Positions
        long_short_netural = total_trade_volume.apply(lambda x: ["LONG", float(x)] if x > 0 else (["SHORT", float(x)] if x < 0 else ["NEUTRUAL", float(x)])).to_list()
        self.trade_positions.loc[date] = list(np.array(long_short_netural).T.reshape(1,4)[0])
        
        # price * trade volume from trade history and current postion/price
        price_x_vol_history = self.trade_history.apply(lambda x: -(x["Price"] * x["Trade Volume"]) if x["Action"] == "BUY" else x["Price"] * x["Trade Volume"], axis=1).sum()
        price_x_vol_current = (self.trade_positions.iloc[-1]["Trade Volume"].astype(float) * self.price_data.loc["2025-02-14 18:23"]["Price"]).sum()

        # update PnL without commisions
        self.PnL_without_commisions = price_x_vol_history + price_x_vol_current

        # update PnL 
        self.PnL = self.PnL_without_commisions - self.total_commission_costs

        # pass
        pass    

    def liquidatePositions(self):
        pass  

    #######################################################
    ## Plot functions

    def plotTradeHistory(self):
        pass

    #######################################################
    ## risk functions

    



