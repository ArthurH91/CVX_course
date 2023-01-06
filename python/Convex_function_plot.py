import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-100,-2,200)

f = lambda X : (X**2 + 1 ) / (X + 2)

x1 = np.linspace(-0.9,0.9,200)

f1 = lambda X : (1 ) / (1 - X**2)

x2 = np.linspace(-500,500,10000)

plt.subplot(221)
plt.plot(x,f(x))

plt.subplot(222)
plt.plot(x1,f1(x1))

plt.subplot(223)
plt.plot(x2,np.cosh(x2))

plt.show() 