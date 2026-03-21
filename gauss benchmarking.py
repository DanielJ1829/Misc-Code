import numpy as np
from GaussJordanElimination import get_solution_vector
from test_cases_gauss import build_large_suite
import time

#this code checks whether each type of augmented matrix returns the matrix it should return.
#note it does not check whether the solution itself is correct due to time complexity

if __name__ == '__main__':
    for A,b,name in build_large_suite():
        print(name, A.shape, "->")
        start = time.perf_counter()
        solution = get_solution_vector(A,b)
        end = time.perf_counter()
        print(solution, 'Time taken: {:.3f}'.format(end-start))