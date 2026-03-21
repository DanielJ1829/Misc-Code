import numpy as np

#Matrix goes here
rng = np.random.default_rng(seed=0)
A = rng.normal(size=(3,3))


def LU_decomp(A):
    #for a 3x3 matrix:
    L = np.array([[1,0,0],
                 [1,1,0],
                 [1,1,1]])
    U = np.array([[1,1,1],
                  [0,1,1],
                  [0,0,1]])
    L,U = L.astype(float),U.astype(float)
    for i in range(3):
        U[0,i] = A[0,i]
    for i in range(2):
        L[i+1,0] = A[i+1,0]/U[0,0]
    for i in range(2):
        U[1,i+1] = A[1,i+1]-L[1,0]*U[0,i+1]
        if U[1,i+1] == 0:
            return 'Error'
    if U[1,1] == 0:
        return 'error, would need to permute rows for this to work'
    L[2,1] = (A[2,1]-L[2,0]*U[0,1])/U[1,1]
    U[2,2] = A[2,2]-L[2,0]*U[0,2]-L[2,1]*U[1,2]
    return L,U

rng = np.random.default_rng(seed=0)
A = rng.normal(size=(3,3))
L,U = LU_decomp(A)

print(A)
print(L@U)
print(L@U-A)
print(L,U)