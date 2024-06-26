import numpy as np
import matplotlib.pyplot as plt

stores = ("Cửa hàng 1", "Cửa hàng 2", "Cửa hàng 3", "Cửa hàng 4", "Cửa hàng 5")
revenue = (72, 40, 33, 90, 100)

plt.bar(stores, revenue, color=[ 'yellow'])
plt.title("Doanh thu bán hàng trong tháng")
plt.xlabel("Số lượng cửa hàng")
plt.ylabel("Doanh thu (Triệu đồng)")
plt.show()  