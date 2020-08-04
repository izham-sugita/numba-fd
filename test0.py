#! /usr/bin/env python3
import numba

@numba.cuda.jit
def gpu_cos(x, out):
    # Assuming 1D array
    start = numba.cuda.grid(1)
    stride = numba.cuda.gridsize(1)
    for i in range(start, x.shape[0], stride):
        out[i] = math.cos(x[i])
