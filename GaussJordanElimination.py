#low level code that allows us to take any matrix, puts it into reduced row echelon form
#(then solves the system)
import numpy as np  #but not linear algebra functions since this is low level
from sympy import symbols, sympify   #for formatting in the free variable case


#example matrices and solution vectors go here
'''A = np.array([[1, 2],
               [2, 4],
               [0, 1],
               [1, 0]])
b = np.array([10, 20, -1, 3])'''
def rref(A,b):
    n, m = A.shape  #returns the number of rows (n) and the number of columns (m)
    augmented = np.column_stack((A,b))  #appends vector b to matrix A to form the augmented matrix
    augmented = augmented.astype(float)
    #need to get the highest value (in magnitude) as the pivot element each time
    #need to swap rows so that this happens

    #forward step (to get ref) - gaussian elimination
    for i in range(min(n,m)):
        pivot_row = i
        max_val = abs(augmented[i][i])   #goes through the diagonals
        for k in range(i+1,n):          #goes down from each diagonal to search for higher value pivots
            if abs(augmented[k][i]) > max_val:
                max_val = abs(augmented[k][i])
                pivot_row = k
        if pivot_row != i:
            augmented[i], augmented[pivot_row] = augmented[pivot_row].copy(), augmented[i].copy()  #swaps the rows
        # If pivot is (numerically) zero, skip this column
        if abs(augmented[i][i]) < 1e-10:
            continue  # don’t try to normalize or eliminate
        pivot = augmented[i][i]
        augmented[i] = augmented[i]/pivot  #set the pivot equal to 1

        for j in range(i+1,n):
            factor = augmented[j][i]  #finds the value of the elements in the rows below the pivot
            augmented[j] = augmented[j] - factor*augmented[i]   #makes the element below the pivot 0
    #backward to step to attain reduced row echelon form after attaining row echelon form

    for i in range(n-1,-1,-1):  #iterating back up the rows
        pivot_col = np.where(abs(augmented[i, :-1]) > 1e-10)[0]  #selects the first non-zero element along the row
        if pivot_col.size == 0:
            continue                    #this allows us to skip any rows that have all non zero rows
        pivot_col = pivot_col[0]        #indexes the pivot correctly (the first non-0 value) (eliminates the all zero row case)
        for j in range(i-1,-1,-1):      #iterates up through
            factor = augmented[j][pivot_col]    #sets our factor to the
            augmented[j] = augmented[j] - augmented[i]*factor    #normalises the pivot
    return augmented

def get_solution(augmented):
    #return the solution (after determining its nature) using the reduced row echelon form)

    n, x = augmented.shape   #n is the number of rows, x is the number of columns + 1 (as this is an augmented matrix)
    m = x-1                 #m is the number of columns in the A matrix.

    #get pivots
    pivot_cols = []
    for i in range(n):          #iterating through the rows
        row = augmented[i,:-1]          #iterating the the rows of the matrix up to the end of the A matrix
        nz = np.where(abs(row)>1e-10)[0]  #gets the first part of the array after finding the indices of the non zero entries
        if nz.size>0:
            pivot_cols.append(nz[0])      #takes the first element
    pivot_cols = set(pivot_cols)        #for uniqueness
    #check for inconsistency:
    for i in range(n):
        if np.all(augmented[i, :-1] < 1e-10) and abs(augmented[i, -1]) > 1e-10:
            return 'The system is inconsistent, so has no solution!'
    #determine if we have a unique solution:
    if len(pivot_cols)==m:
        return augmented[:m, -1]

    #free variable case:
    free_vars = [j for j in range(m) if j not in pivot_cols]
    solution = {}
    for k, fv in enumerate(free_vars):  #k gives you the free variable index and fv gives you the column index
        solution[fv] = f"t{k+1}"
    #back substituing:
    for i in range(len(pivot_cols)):
        pivot_col = list(pivot_cols)[i]
        row = augmented[i, :-1]         #as before, gets all the elements/cols in a row in A
        rhs = augmented[i, -1]          #gets the corresponding element in b
        expression = f"{rhs:.3f}"
        for j in free_vars:
            coefficient = row[j]        #gets the free variable to then subtract it from the b value in the b vector
            if abs(coefficient) > 1e-10:
                expression += f" + {(-coefficient):.3f}*{solution[j]}"
        solution[int(pivot_col)] = expression
    solution = dict(sorted(solution.items()))
    solution = {f"x{k}": solution[k] for k in sorted(solution)}

    solutionlist = []
    for i in range(m):
        solutionlist.append(sympify(solution.get(f"x{i}")))
    return solutionlist

def get_solution_vector(A,b):
    augmented = rref(A,b)
    solution_vector = get_solution(augmented)
    return solution_vector

'''augmented = rref(A,b)
print(augmented, '- Augmented Matrix')
print(get_solution(augmented))'''
