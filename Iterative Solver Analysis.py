import numpy as np
import matplotlib.pyplot as plt
from Jacobi_Iteration_Method import JacobiIteration
from test_cases_gauss import unique_large
from GaussJordanElimination import get_solution_vector
#analysis of how errors converge for jacobi iteration

A,b,name = unique_large(100,seed=0)
mean_error = []
for i in range(1,50):
    x = JacobiIteration(A,b,i)
    x_actual = np.linalg.solve(A,b)
    errors = [float(abs(x[i]-x_actual[i])) for i in range(len(x))]
    mean_error.append(np.linalg.norm(x - x_actual))

x_values = [i for i in range(1,50)]
y_values = mean_error
ax = plt.subplot()
ax.plot(x_values,y_values)
ax.set_title('Error Convergence Analysis: Jacobi Iteration')
ax.set_ylabel("Error at the n'th iteration")
ax.set_xlabel("iteration number")
ax.text(
    0.97, 0.97,  # x, y position in axes coordinates
    "Note: Although the error should\n"
    "converge to 0, floating points\n"
    "prevent this. We instead see it\n"
    "converge to a point close to 0.",
    transform=ax.transAxes,   # use axes coordinates so that 0.95 always means 95% of the way along the x&y axes
    fontsize=9,
    va='top', ha='right',            #the vertical and horizontal alignments of the text box
    bbox=dict(facecolor='white', alpha=0.8, edgecolor='black')
)
plt.show()
