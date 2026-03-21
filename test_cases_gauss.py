import numpy as np
import time
rng = np.random.default_rng(0)

# 1 - large square full rank matrices (giving a unique solution): 200×200
def unique_large(n=200, seed=0):
    rng = np.random.default_rng(seed)
    A = rng.normal(size=(n, n))         #generates an nxn array of random numbers starting w/seed 0,
                                        # normally distributed about 0 w/std 1 (rng.normal defaults to this)
    A += n * np.eye(n)  # make it strongly diagonally dominant → invertible  (np.eye is the diagonal matrix)
    #the sum of off diagonal entries is of the order sqrt(n) due to the law of large numbers, smaller than the diagonal
    #entries of n; making the matrix strongly diagonally dominant
    x_true = rng.normal(size=n)         #arbitrarily assigns a solution vector to A
    b = A @ x_true                      #multiplies the true solution vector by A, forcing b to be the solution
    return A, b, "unique_solution"

# 2) large overdetermined consistent matrices with redundancies: 300×80 (rank 80)
def redundant_overdetermined_consistent(m=300, n=80, seed=1):   #(initialised pseudo rng at 1)
    rng = np.random.default_rng(seed)
    # Builds n independent rows, then adds (m-n) rows that are linear combinations of the independent rows
    R = rng.normal(size=(n, n))           # square block, full rank (the probability of this is ~ 1)
    #(since the determinant of a random continuous matrix is itself a continous random variable; the probability of
    #R's determinant being 0 is close enough to 0 for p(fullrank) ~ 1 (full rank matrices require non 0 determinants)
    C = rng.normal(size=(m - n, n))       # coeffs to form (m-n) redundant rows of length n
    extras = C @ R                        # makes each extra row a multiple of R's rows; making the matrix redundant
    A = np.vstack([R, extras])            # adds on the redundant rows to the matrix
    x_true = rng.normal(size=n)           # arbitrary solution vector
    b = A @ x_true                        # makes the b vector consistent by construction
    return A, b, "redundant_consistent"

# 3) large underdetermined matrices with infinite solutions (and thus w/free variables): 70×200 (rank ≤ 70)
def underdetermined_infinite(m=70, n=200, seed=2):
    rng = np.random.default_rng(seed)
    A = rng.normal(size=(m, n))           # rank ≤ m < n → free variables
    x_true = rng.normal(size=n)
    b = A @ x_true                        # consistent, infinitely many solutions
    return A, b, "underdetermined_infinite"

# 4) large square rank-deficient consistent matrices (w/free variables): 150×150 with rank 140
def square_rank_deficient_consistent(n=150, r=140, seed=3):
    rng = np.random.default_rng(seed)
    P = rng.normal(size=(n, r))            # since rank(PQ) <= min(rank(P), rank(Q)) this gives us a rank of r or lower.
    Q = rng.normal(size=(r, n))
    A = P @ Q                              # rank ≤ r < n
    x_true = rng.normal(size=n)            # using normal(0,1), creates a random solution vector
    b = A @ x_true                         # forces the solution and results in a consistent solution w/free variables
    return A, b, "square_rank_deficient_consistent"

# 5) large overdetermined inconsistent matices: start consistent then break one redundant row
def overdetermined_inconsistent(m=300, n=80, bump=1.0, seed=4):
    A, b, _ = redundant_overdetermined_consistent(m, n, seed)
    # Make sure we nudge a row that is *redundant*, i.e., past the first n
    k = m - 1
    b[k] = b[k] + bump                     # this violates the linear dependence on the rhs;
    # as A[k] in the redundant matrix before was a combination of previous rows, b[k] was also consistent since it was
    # a linear combination of A's rows. Doing this violates that property, forcing the system to be inconsistent.
    return A, b, "overdetermined_inconsistent"

# (Bonus) 6) large square inconsistent matrix using a duplicated row with different RHS: 180×180
def square_inconsistent(n=180, seed=5):
    rng = np.random.default_rng(seed)
    A = rng.normal(size=(n, n))
    # let row 1 be a duplicate of row 0 so we can have inconsistency (make the 1st/2nd b vector terms
    # different to ensure this)
    A[1] = A[0]
    x_true = rng.normal(size=n)
    b = A @ x_true
    b[1] = b[0] + 1.0                      # contradiction on duplicated row to force inconsistency
    return A, b, "square_inconsistent"

# --- Build a suite you can loop over ---
def build_large_suite():
    cases = []
    cases.append(unique_large())                        #literally just appends all the functions into cases
    cases.append(redundant_overdetermined_consistent())
    cases.append(underdetermined_infinite())
    cases.append(square_rank_deficient_consistent())
    cases.append(overdetermined_inconsistent())
    cases.append(square_inconsistent())
    return cases
