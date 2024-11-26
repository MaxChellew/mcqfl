import numpy as np
import scipy as sp

def callV(St, k, tau, sigma, r):

    d1 = np.log(St/K)

    return St*sp.stats.norm.cdf(d1)