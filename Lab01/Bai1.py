import matplotlib.pyplot as plt
import numpy as np

x_points = np.array([1,3,6,9,14])
y_points = np.array([10,9,23,18,50])

plt.plot(x_points, y_points, linestyle = ':', color = 'g')
plt.show()