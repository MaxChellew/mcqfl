### BlackScholes Libary

# Author: Max Chellew

## Libarys

# Import Libarys
import numpy as np
import scipy as sp
import mcp

## Option Price Functions

# Vanilia Call Option Price
def callV(St, K, tau, sigma, r):

    # set d1 and d2 values
    d1 = ( np.log(St/K) + (r + 0.5*(sigma**2))*tau ) / ( sigma*np.sqrt(tau) )
    d2 = ( np.log(St/K) + (r - 0.5*(sigma**2))*tau ) / ( sigma*np.sqrt(tau) )

    # return price
    return St*sp.stats.norm.cdf(d1) - K*np.exp(-r*tau)*sp.stats.norm.cdf(d2)


# Vanilia Put Option Price
def putV(St, K, tau, sigma, r):

    # set d1 and d2 values
    d1 = ( np.log(St/K) + (r + 0.5*(sigma**2))*tau ) / ( sigma*np.sqrt(tau) )
    d2 = ( np.log(St/K) + (r - 0.5*(sigma**2))*tau ) / ( sigma*np.sqrt(tau) )

    # return price
    return -St*sp.stats.norm.cdf(-d1) + K*np.exp(-r*tau)*sp.stats.norm.cdf(-d2)

## Impied Volatility Functions