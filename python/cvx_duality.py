import numpy as np
import matplotlib.pyplot as plt
import cvxpy as cvx

# Init (data given in the problem)

U1 = -2
U2 = -3

P = 2 * np.array([[1, -0.5], [- 0.5, 2]])
q = np.array([-1, 0])
A = np.array([[1,2], [1, -4], [- 1, - 1]])
b = np.array([U1, U2, 5])

x = cvx.Variable(2)

# Solve QP ( min 1/2 * x.T * P * x + q.T * x s.t. A*x <= b )

constraints = [A @ x <= b]

objective = cvx.Minimize(1/2 * cvx.quad_form(x, P) + q.T @ x )
prob = cvx.Problem(objective, constraints)
result = prob.solve()

# Results

print("status:", prob.status)
print("optimal value", prob.value)
print("optimal var", x.value)
