from numba import jit
import numba as nb
import numpy as np

size = 3
matrix = np.array([[0.0, 1.0, 2.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
b = np.ndarray((3,3) ,dtype=np.float64)
#b = np.zeros((size,size))

#@jit(nopython=True)
@jit(nb.float64(nb.float64[:,:]))
def test(jitmatrix):
    _total = 0
    for i in range(size):
        for j in range(size):
            # _total += jitmatrix[j,i]  # note the change in indexing, which is faster
            jitmatrix[j,i] = 1  # note the change in indexing, which is faster

    return _total #just like in C


test(matrix)
print(matrix)
test(b)
print(b)
