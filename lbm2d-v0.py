import numpy as np
from numba import jit, njit, prange

def information():
    import os
    filename = os.path.basename(__file__)
    print("This is a prototype of LBM code file: %s"%(filename))

@njit(nogil=True,parallel=True)
def par_init_array(a):
    for i in prange(N):
        a[i] = np.random.random()

@njit(nogil=True,parallel=True)
def par_vec_add(a,b,c,N):
    for i in prange(N):
        c[i] = a[i] + b[i]
    

if __name__ == "__main__":

    information()
    N = 4096*4096*4
    a = np.ndarray((N))
    b = np.ndarray((N))
    c = np.zeros_like(a)
    par_init_array(a)
    par_init_array(b)
    print()
    print(a)
    print(b)
    print(c)
    print(N)
    print()
    for i in range(10):
        par_vec_add(a,b,c,N)

    print(c)
