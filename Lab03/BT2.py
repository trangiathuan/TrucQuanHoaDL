import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("D:/NTTU/Trực Quan Hóa Dữ Liệu/LAB/LAB03/tips.csv")
# Nhóm dữ liệu theo ngày trong tuần và tính tổng tiền tip cho mỗi ngày
day_totals = data.groupby("day")["tip"].sum()

# Trích xuất nhãn ngày và tổng số tiền típ
day_labels = day_totals.index.to_numpy()
total_tips = day_totals.to_numpy()

# Tạo biểu đồ thanh
plt.figure(figsize=(7, 6))  # Set figure size for better readability
plt.bar(day_labels, total_tips, color=["blue"])
# Tùy chỉnh giao diện biểu đồ
plt.xlabel("Ngày trong tuần")
plt.ylabel("Tổng tiền thưởng (Tip)")
plt.title("Tổng tiền thưởng theo ngày trong tuần")

plt.tight_layout() 
plt.show()