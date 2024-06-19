import matplotlib.pyplot as plt
import numpy as np

x_points = np.array([1,3,7,13])
y_points = np.array([9,23,15,45])

a_points = np.array([1,3,6,9,15])
b_points = np.array([10,9,23,17,50])


plt.plot(x_points, y_points, linestyle = '--', color = 'r')
plt.plot(a_points, b_points, linestyle = ':', color = 'g')
plt.show()