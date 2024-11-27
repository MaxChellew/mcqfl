### BlackScholes Libary
# Author: Max Chellew

## Libarys

# Import Libarys
import numpy as np
import scipy as sp
import BlackScholes as bs

def yes():
    return bs.callV(100, 110, 1, 0.5, 0.045)