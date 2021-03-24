from numba import cuda, float32
import math
import time

@cuda.jit
def matmul(A, B, C):
    """Perform square matrix multiplication of C = A * B
    """
    i, j = cuda.grid(2)
    if i < C.shape[0] and j < C.shape[1]:
        tmp = 0.
        for k in range(A.shape[1]):
            tmp += A[i, k] * B[k, j]
        C[i, j] = tmp


print(cuda.select_device(0))

import numpy as np

N = 4096
A = np.random.rand(N,N)
B = np.identity(N)
C = np.zeros_like(A)
#print(A)

threadsperblock = (16, 16)
blockspergrid_x = math.ceil(A.shape[0] / threadsperblock[0])
blockspergrid_y = math.ceil(A.shape[1] / threadsperblock[1])
blockspergrid = (blockspergrid_x, blockspergrid_y)

ts = time.time()
matmul[blockspergrid,threadsperblock](A,B,C)
te = time.time()
elp = te -ts
gflops = ( ( float(N)**3 ) / elp ) * 10.0e-9 
print("Elapsed time: ",elp, "secs")
print("Throughput ", gflops, "GFLOPS ") 
print()
#print(C)
