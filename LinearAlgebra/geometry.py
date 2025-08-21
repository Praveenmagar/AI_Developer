import numpy as np
import matplotlib.pyplot as plt

u = np.array([2, 1])
v = np.array([1, 3])

plt.quiver(0, 0, u[0], u[1], angles='xy', scale_units='xy', scale=1, color='r', label='u')
plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='b', label='v')
plt.xlim(-1, 4)
plt.ylim(-1, 4)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.legend()
plt.show()
