import matplotlib.pyplot as plt
import numpy as np

x_points = np.array([1,2,3,5,7])
y_points = np.array([5,1.5,5,20,10])

plt.plot(x_points, y_points,'bD--', color = 'r')
plt.show()