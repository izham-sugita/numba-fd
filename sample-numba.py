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
        
    return trace # a+trace?


#first warm up
start = time.time()
a = go_fast(x)
end = time.time()
print(a)
print("Elapsed time with compilation: %s" %(end-start))

#after compilation
start = time.time()
a = go_fast(x)
end = time.time()
print(a)
print("Elapsed time after compilation: %s" %(end-start))

#test compiled module
start = time.time()
a = foo.go_fast_mod(x)
end = time.time()
print(a)
print("Elapsed time for first run module compilation: %s" %(end-start))

#test compiled module
start = time.time()
a = foo.go_fast_mod(x)
end = time.time()
print(a)
print("Elapsed time for second run module compilation: %s" %(end-start))

#test compiled module with numba
start = time.time()
a = foo.go_fast_numba(x)
end = time.time()
print(a)
print("Elapsed time for first run numba in module compilation: %s" %(end-start))

#test compiled module with numba
start = time.time()
a = foo.go_fast_numba(x)
end = time.time()
print(a)
print("Elapsed time for second run numba in module compilation: %s" %(end-start))
