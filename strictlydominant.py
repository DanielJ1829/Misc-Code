import numpy as np
#an algorithm for determining whether a (square) matrix is strictly diagonally dominant or not
#a square matrix M is said to be strictly diagonally dominant matrix when M[i,i]>=np.sum(M[i,j]) for all j != i
#the way this is done in python is M[i,i]
def strictlydom(A):
    """
    :param A: a square matrix
    :return: True or False dependent on whether the matrix is stictly diagonally dominant or not
    """
    #check if the matrix is square:
    if len(A) != len(A[0]):
        return 'Matrix is non-square; test is invalid'
    byrow= []
    for i in range(len(A)):
        byrow.append(2*abs(A[i,i])-np.sum(abs(A[i])))
    if all(x>=0 for x in byrow):
        return True
    else:
        return False

#insert matrix here
M = np.array([[3,-3,1],
             [1,3,1],
             [1,1,3],
             ])
a = strictlydom(M) #determine result
print(a)