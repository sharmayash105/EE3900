import numpy as np
from matplotlib import pyplot as plt

n = 100000
s = np.linspace(0,10000000, n)
r1 = 1
r2 = 2
c = 1e-6
h = r1/(r1 + r2 + s*c*r1*r2)
plt.plot(s,h)
plt.grid()
plt.xlabel('s')
plt.ylabel('H(s)')
plt.show()
