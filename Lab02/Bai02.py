import matplotlib.pyplot as plt
import numpy as np

x_green = np.array([0,1,2,3,4])
y_green = np.array([1,2,3,4,10])

x_red = np.array([0,1,2,3,4])
y_red = np.array([10,4,3,2,1])

x_blue = np.array([2.5,2.5,2.5,1.5,0.5])
y_blue = np.array([1,3,5,7,10])

x_yellow = np.array([0,1.4,2,5,6])
y_yellow = np.array([3,2,3,5,8])


plt.title("Line in Python Matplotlib")
plt.ylabel("Y")
plt.xlabel("X")

plt.grid(True)
plt.plot(x_green, y_green, 'go-', color = 'g', label = 'Green')
plt.plot(x_red, y_red, 'go-', color = 'r',label = 'Red')
plt.plot(x_blue, y_blue, 'go-', color = 'b',label = 'Blue')
plt.plot(x_yellow, y_yellow,'go-', color = 'y',label = 'Yellow')
plt.legend()
plt.show()