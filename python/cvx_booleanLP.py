import numpy as np
import matplotlib.pyplot as plt
import cvxpy as cvx


# Init (datas given by the problem)
np.random.seed(0)
n = 100
m = 300
A = np.random.rand(m, n)
b = A @ np.ones((n, 1)) / 2
c = -np.random.rand(n, 1)
x0 = np.random.randn(n)
bb = A @ x0
x = cvx.Variable(n)
print(A@x)
# print(bb)
# solve LP relaxation
# x = cvx.Variable(n)
constraints = [A * x <= b, 
               x >= 0, x <= 1]

# objective = cvx.Minimize(c.T @ x)
# prob = cvx.Problem(objective, constraints)
# result = prob.solve()
# xrlx = x.value
# L = result

# print(L)

# # sweep over threshold & round
# thres = np.arange(0, 1.01, 0.01)
# maxviol = np.zeros(len(thres))
# obj = np.zeros(len(thres))
# for i in range(len(thres)):
#     xhat = (xrlx >= thres[i])
#     maxviol[i] = np.max(A @ xhat - b)
#     obj[i] = c.T @ xhat

# # find least upper bound and associated threshold
# i_feas = np.where(maxviol <= 0)[0]
# U = np.min(obj[i_feas])
# t = np.min(i_feas)
# min_thresh = thres[t]

# # plot objective and max violation versus threshold
# fig, axs = plt.subplots(2, 1)
# axs[0].plot(thres[:t-1], maxviol[:t-1], 'r', thres[t:], maxviol[t:], 'b', linewidth=2)
# axs[0].set_xlabel('threshold')
# axs[0].set_ylabel('max violation')
# axs[1].hold(True)
# axs[1].plot(thres, L*np.ones(len(thres)), 'k', linewidth=2)
# axs[1].plot(thres[:t-1], obj[:t-1], 'r', thres[t:], obj[t:], 'b', linewidth=2)
# axs[1].set_xlabel('threshold')
