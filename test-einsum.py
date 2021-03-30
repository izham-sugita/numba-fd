#https://tensorchiefs.github.io/dlday2018/tutorial/einsum.html
import numpy as np

#initiate matrix
N = 3
mat = np.random.rand(N,N)
matb = np.identity(N)
print(mat)
print(type(mat))
vec = np.random.rand(N)
print(vec)
print(type(vec))

#matrix multiplicatio by Einstein summation
vec2 = np.einsum('ij, j', matb,vec)
print(vec2)
