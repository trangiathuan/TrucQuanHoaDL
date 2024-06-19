import matplotlib.pyplot as plt
import numpy as np

x = np.array([20,22,24,26,28,30])
y_xang = np.array([5,3,5,4,5,5])
y_dau = np.array([4,4.5,5,3,4,7])
y_nhot = np.array([5,4,6,4,6,8])

plt.plot(x, y_xang, linestyle = '-', color = 'b', label = 'xang')
plt.plot(x, y_dau, linestyle = '-', color = 'g', label = 'dau')
plt.plot(x, y_nhot, linestyle = '-', color = 'r', label = 'nhot')

plt.title('Biểu đồ nhiên liệu trong nước (năm 2020)')
plt.xlabel('Tháng')
plt.ylabel('Giá nhiên liệu (VND)')

plt.legend()
plt.show()

