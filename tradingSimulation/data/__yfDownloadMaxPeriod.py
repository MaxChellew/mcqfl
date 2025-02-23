#######################################################

# Author: Max Chellew
# Libary: emarci

#######################################################

# Global Libary imports: numpy, pandas
import yfinance as yf

# Local Libary imports: NaN

#######################################################

# function: yfDownloadMaxPeriod
# yahoo Finance Download Max Period
def yfDownloadMaxPeriod(tickers, interval):

    # Download yf data
    df = yf.download(tickers, period="max", interval=interval)

    # re-format dataframe
    df = df.drop(columns=["Open", "Volume"])
    df = df.rename(columns={"Close": "Price"})
    df.index.name = "Date"
    df.index = df.index.strftime('%Y-%m-%d %H:%M')

    # return dataframe
    return df

