import numpy as np
import matplotlib.pyplot as plt
# import cvxpy as cvx

f0 = lambda x: x**2 + 1 
f1 = lambda x: (x - 2) * (x - 4)

L = lambda x,lamb : x ** 2 * (1 + lamb) - 6 * lamb * x + 8 * lamb + 1

def is_inf_zero(y):
    ycopy = np.copy(y)
    n = len(ycopy)
    for k in range(n):
        if ycopy[k] > 0:
            ycopy[k] = 0
    return ycopy



t = np.linspace(-5,5,200)
y1 = f0(t)
y2 = (f1(t))
L1 = L(t,1)
L2 = L(t,2)
L3 = L(t,3)
L4 = L(t,4)

plt.plot(t,y1, label="F0")
plt.plot(t,y2, label="F1")
plt.plot(t,L1, label="L1")
plt.plot(t,L2, label="L2")
plt.plot(t,L3, label="L3")
plt.plot(t,L4, label="L4")


plt.axhline(0, color='black')
plt.legend()
plt.show()
