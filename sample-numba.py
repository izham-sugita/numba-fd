from numba import jit
import numpy as np
import time

import foo

x = np.arange(10000).reshape(100,100)

@jit(nopython=True)
def go_fast(a):
    trace=0
    for i in range(a.shape[0]):
        trace +=np.tanh(a[i,i])
        
    return a+trace


#first warm up
start = time.time()
go_fast(x)
end = time.time()
print("Elapsed time with compilation: %s" %(end-start))

#after compilation
start = time.time()
go_fast(x)
end = time.time()
print("Elapsed time after compilation: %s" %(end-start))

#test compiled module
start = time.time()
foo.go_fast_mod(x)
end = time.time()
print("Elapsed time for first run module compilation: %s" %(end-start))

#test compiled module
start = time.time()
foo.go_fast_mod(x)
end = time.time()
print("Elapsed time for second run module compilation: %s" %(end-start))

#test compiled module with numba
start = time.time()
foo.go_fast_numba(x)
end = time.time()
print("Elapsed time for first run numba in module compilation: %s" %(end-start))

#test compiled module with numba
start = time.time()
foo.go_fast_numba(x)
end = time.time()
print("Elapsed time for second run numba in module compilation: %s" %(end-start))
