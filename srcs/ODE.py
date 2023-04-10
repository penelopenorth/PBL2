# from __future__ import print_function
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np
import time
  
# Constants
k1 = 200
k2 = 1000
k3 = 0.05
A0 = 1.0
B0 = 0.0
C0 = 1.0
D0 = 0.0

y0 = [A0, B0, C0, D0]

tspan = np.linspace(0, 100)


def odefunc(y0, t):
    A, B, C, D = y0
    dA = -k1*A-k2*A*C+k3*D
    dB = k1*A
    dC = -2*k2*A*C+2*k3*D
    dD = k2*A*C - k3*D
    return [dA, dB, dC, dD]
start = time.time()
y, info = odeint(odefunc, y0, tspan, full_output=True)
print(f'Time elapsed: {(time.time() - start)*1000:.2f}ns')
method = info['mused']
print(f'Method used: {method[0]}; 1 = adams, 2 = bdf')

labels = ['A', 'B', 'C', 'D']
for i in range(4):
    plt.plot(tspan, y[:, i], label = labels[i])
plt.legend()
plt.xlabel('Time')
plt.ylabel('Conc')
plt.show()





