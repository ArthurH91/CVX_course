import cvxpy as cp

# Create two scalar optimization variables.
x1 = cp.Variable()
x2 = cp.Variable()

# Create two constraints.
constraints = [2 * x1 + x2 >= 1,
               x1 + 3 * x2 >= 1,
               x1 >= 0,
               x2 >= 0]

# Form objective.
obj = cp.Minimize((x1 ** 2 + 9 * x2 ** 2)) ### A changer avec la bonne fonction

# Form and solve problem.
prob = cp.Problem(obj, constraints)
prob.solve()  # Returns the optimal value.
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal var", x1.value, x2.value)

# Import packages.
# import cvxpy as cp
# import numpy as np

# # Generate a random non-trivial linear program.
# m = 15
# n = 10
# np.random.seed(1)
# s0 = np.random.randn(m)
# lamb0 = np.maximum(-s0, 0)
# s0 = np.maximum(s0, 0)
# x0 = np.random.randn(n)
# A = np.random.randn(m, n)
# b = A @ x0 + s0
# c = -A.T @ lamb0

# # Define and solve the CVXPY problem.
# x = cp.Variable(n)
# prob = cp.Problem(cp.Minimize(c.T@x),
#                  [A @ x <= b])
# prob.solve()
