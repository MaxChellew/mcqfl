#######################################################

# Author: Max Chellew
# Libary: emarci

#######################################################

# Global Libary imports: numpy, pandas
import yfinance as yf

# Local Libary imports: NaN

#######################################################

# function: yfDownloadD
# yahoo Finance Download Daily Price
def yfDownloadAnyDate(tickers, start, end):

    # Download yf data
    df = yf.download(tickers, start, end, "1d")

    # re-format dataframe
    df = df.drop(columns=["Open", "Dividends", "Volume", "Stock Splits"])
    df = df.rename(columns={"Close": "Price"})
    df.index.name = "Date"
    df.index = df.index.strftime('%Y-%m-%d %H:%M')

    # return dataframe
    return df
