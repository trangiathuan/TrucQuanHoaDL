import matplotlib.pyplot as plt
import numpy as np
# Dữ liệu
x1 = [0,1,4,6,5]
y1 = [1,2,3,5,6]

x2 = [0,1,2,7,8]
y2 = [10,4,3,2,1]

x3 = [2.5, 2.5, 4, 1.5, 0.5]
y3 = [1, 3, 5, 7, 8]

# Tạo biểu đồ line
plt.figure(figsize=(10,3))  

# Biểu đồ 1
plt.subplot(1,3,1)  
plt.plot(x1, y1, 'go-', label='green color', color = 'g')  
plt.title('green color')  
plt.xlabel('X1')  
plt.ylabel('Y1')  
plt.grid(True) 
plt.legend()

# Biểu đồ 2
plt.subplot(1, 3, 2)  
plt.plot(x2, y2, 'go-', label='Red color', color ='r') 
plt.title('red color')  
plt.xlabel('X2')  
plt.ylabel('Y2') 
plt.grid(True)  
plt.legend()

# Biểu đồ 3
plt.subplot(1, 3, 3) 
plt.plot(x3, y3, 'go-', label='Blue color', color = 'b')
plt.title('blue color') 
plt.xlabel('X3')  
plt.ylabel('Y3')  
plt.grid(True)  
plt.legend()  
plt.show()