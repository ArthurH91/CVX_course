import numpy as np
import matplotlib.pyplot as plt
import cvxpy as cvx

# First exercise
# Init (data given in the problem)

# d1 & d2 parameters varying between - 0.1 & 0.1. For the 2nd exercise only.
d1 = 0
d2 = 0

U1 = -2 + d1
U2 = -3 + d2

P = 2 * np.array([[1, -0.5], [- 0.5, 2]])
q = np.array([-1, 0])
A = np.array([[1, 2], [1, -4], [- 1, - 1]])
b = np.array([U1, U2, 5])

x = cvx.Variable(2)

# Solve QP ( min 1/2 * x.T * P * x + q.T * x s.t. A*x <= b )
constraints = [A @ x <= b]
objective = cvx.Minimize(1/2 * cvx.quad_form(x, P) + q.T @ x)
prob = cvx.Problem(objective, constraints)
result = prob.solve()
dual_variable1 = constraints[0].dual_value
p_pred = prob.value
p_diff = 8.222222222222223 - p_pred

# Results
print("First exercise : ")
print(f"status: {prob.status}")
print(f"optimal value : {prob.value}")
print(f"optimal var : {x.value}")
print(f"dual variables : {dual_variable1}")
print(f"p_diff : {p_diff}")
print(" -------------------------------------------")


# 2nd exercise

# NE FONCTIONNE PAS CAR CVXPY C'EST DE LA MERDE (NE CREER PAR UN AUTRE PROBLEME PAR DESSUS L'ANCIEN, DOIT DONC
# LE FAIRE A LA MAIN).

# d1 = [-0.1, 0, 0.1]
# d2 = [-0.1, 0, 0.1]

# P = 2 * np.array([[1, -0.5], [- 0.5, 2]])
# q = np.array([-1, 0])
# A = np.array([[1, 2], [1, -4], [- 1, - 1]])
# b = np.array([U1, U2, 5])


# diff_p_list = [] # list of p_exact - p_pred

# for d in d1:
#     U1 = -2 + d # pertubation
#     print(f"U1 : {U1}")
#     for dd in d2:
#         x1 = cvx.Variable(2)
#         U2 = -3 + dd
#         print(f"U2 : {U2}")
#         constraints1 = [A @ x1 <= b]
#         objective1 = cvx.Minimize(1/2 * cvx.quad_form(x1, P) + q.T @ x1)
#         prob1 = cvx.Problem(objective1, constraints1)
#         result1 = prob1.solve()
#         p_pred = prob1.value
#         p_diff = p_exact - p_pred
#         print(f"status: {prob1.status}")
#         print(f"optimal value : {p_pred}")
#         print(f"difference between p_exact and p_prediction : {p_diff}")
#         diff_p_list.append(p_diff)
#         x1 = None
#         constraints1 = None
#         objective1 = None
#         prob1 = None
#         result1 = None

# plt.plot(p_diff,'o')
# plt.show()
