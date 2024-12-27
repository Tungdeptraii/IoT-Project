import pandas as pd

# Đọc file CSV vào DataFrame
df = pd.read_csv(r'D:\IoT\IoT-Final_Exam_PID TempBox\Data\data1_sp16.csv')

# Cắt DataFrame từ hàng 4740 trở đi
df_subset = df.iloc[4740:]

# Tính toán các chỉ số thống kê cho PV1 và PV2 từ hàng 4740 trở đi
mean_PV1 = df_subset['PV1'].mean()  # Nhiệt độ trung bình của PV1
median_PV1 = df_subset['PV1'].median()  # Trung vị của PV1
std_PV1 = df_subset['PV1'].std()  # Độ lệch chuẩn của PV1

mean_PV2 = df_subset['PV2'].mean()  # Nhiệt độ trung bình của PV2
median_PV2 = df_subset['PV2'].median()  # Trung vị của PV2
std_PV2 = df_subset['PV2'].std()  # Độ lệch chuẩn của PV2

# Tính giá trị min và max của PV1 và PV2
min_PV1 = df_subset['PV1'].min()  # Giá trị nhỏ nhất của PV1
max_PV1 = df_subset['PV1'].max()  # Giá trị lớn nhất của PV1

min_PV2 = df_subset['PV2'].min()  # Giá trị nhỏ nhất của PV2
max_PV2 = df_subset['PV2'].max()  # Giá trị lớn nhất của PV2

# In kết quả
print(f"Nhiệt độ trung bình PV1: {mean_PV1:.4f} °C")
print(f"Trung vị PV1: {median_PV1:.4f} °C")
print(f"Độ lệch chuẩn PV1: {std_PV1:.4f}")
print(f"Giá trị nhỏ nhất PV1: {min_PV1:.4f} °C")
print(f"Giá trị lớn nhất PV1: {max_PV1:.4f} °C")

print(f"\nNhiệt độ trung bình PV2: {mean_PV2:.4f} °C")
print(f"Trung vị PV2: {median_PV2:.4f} °C")
print(f"Độ lệch chuẩn PV2: {std_PV2:.4f}")
print(f"Giá trị nhỏ nhất PV2: {min_PV2:.4f} °C")
print(f"Giá trị lớn nhất PV2: {max_PV2:.4f} °C")
