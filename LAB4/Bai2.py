import matplotlib.pyplot as plt
import numpy as np

n1 = np.random.randn(20)
n2 = np.random.randn(20)
n3 = np.random.randn(20)
n4 = np.random.randn(20)
 
plt.scatter(n1, n2, marker='v', c='red', label='red')  
plt.scatter(n2, n3, marker='^', c='blue', label='blue')  
plt.scatter(n3, n4, marker='*', c='green', label='green')  
plt.scatter(n4, n1, marker='o', c='orange', label='orange') 

plt.legend(loc = 'lower right', ncol = 2)

plt.tight_layout()

plt.show()