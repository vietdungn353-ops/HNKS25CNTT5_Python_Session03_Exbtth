from datetime import datetime

name = input("Nhập tên bệnh nhân: ")
year_of_birth = int(input("Nhập năm sinh: "))
day_Illness = int(input("Nhập số ngày bệnh: "))
temperature = int(input("Nhập nhiệt độ cơ thể: "))
price = int(input("Nhập chi phí khám: "))

if name.strip() == "":
    print("Tên không được để trống")
elif year_of_birth < 1900 or year_of_birth > datetime.now().year:
    print("Năm sinh không hợp lệ")
elif day_Illness < 0:
    print("Số ngày bệnh không hợp lệ")
elif temperature < 30 or temperature > 45:
    print("Nhiệt độ cơ thể không hợp lệ")
elif price <= 0:
    print("Chi phí khám không hợp lệ")
else:
    print(f"""
        --- KẾT QUẢ ---
        Tên bệnh nhân: {name} 
        Tuổi: {datetime.now().year - year_of_birth}
        Số ngày bệnh: {day_Illness}
        Nhiệt độ cơ thể: {temperature} độ C
    """)

total_price = price*1.1

if temperature > 38 and day_Illness > 3:
    status = "Nguy hiểm"
    if datetime.now().year - year_of_birth > 60:
        priority = "Cấp cứu"
    else:
        priority = "Ưu tiên cao"
elif temperature > 38:
    status = "Sốt cao"
    priority = "Bình thường"
elif temperature > 37.5:
    status = "Sốt nhẹ"
    priority = "Bình thường"
else:
    status = "Bình thường"
    priority = "Bình thường"

total_price = "Cao" if total_price > 500_000 else "Thấp"

print("Tình trạng:", status)
print("Mức độ ưu tiên:", priority)

print("\nTổng chi phí:", price*1.1)
print("Mức chi phí: ", total_price)

