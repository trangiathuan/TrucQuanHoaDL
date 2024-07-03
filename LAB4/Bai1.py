import matplotlib.pyplot as plt
# dataset-1
x1 = [89, 43, 36, 36, 95, 10, 87, 66, 34, 38, 20, 26, 34, 90, 33] 
y1 = [21, 46, 3, 26, 34, 90, 33, 35, 53, 72, 58, 10, 67, 95, 120]
# dataset2
x2 = [26, 29, 48, 20, 56, 2, 48, 20, 56, 36, 66, 72, 20, 56, 2, 47, 40]
y2 = [26, 34, 90, 33, 38, 42, 20, 8, 20, 56, 2, 47, 15, 47, 64, 6, 5]

plt.scatter(x1, y1, c = "pink",
            linewidths = 2,
            marker = "s",
             edgecolors= "red",
              s = 100 )
plt.scatter(x2, y2, c = "yellow",
            linewidths = 2,
            marker = "^",
             edgecolors= "green",
              s = 200 )

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
