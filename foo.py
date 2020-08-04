import numpy as np
from numba import jit

def go_fast_mod(a):
    trace=0
    for i in range(a.shape[0]):
        trace +=np.tanh(a[i,i])
        
    return a+trace

@jit(nopython=True)
def go_fast_numba(a):
    trace = 0
    for i in range(a.shape[0]):
        trace +=np.tanh(a[i,i])

    return a+trace
