# Plotting H(s)

import numpy as np
import matplotlib.pyplot as plt
# import subprocess
# import shlex

def H(s):
    return 5e5/(s + 1.5e6)

S = np.linspace(-6e6, 3e6, 100)

plt.plot(S, H(S))
plt.grid()
plt.title('Transfer Function')
plt.xlabel('$s$')
plt.ylabel('$H(s)$')
plt.show()