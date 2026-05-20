number_employees = int(input("Hãy nhập số lượng nhân viên: "))
i = 0
while i <= number_employees:

    if i == number_employees:
        question = input("Tiếp tục chương trình? (y/n): ")
        if question == "y":
            i = 0
            employees_number = int(input("Hãy nhập số lượng nhân viên: "))
            number_employees = employees_number
        elif question == "n":
            print("Chương trình kết thúc")
            exit()

    id_employees = i+1
    print(f"Nhân viên {id_employees}")
    name = input("Tên nhân viên: ")
    number_work = int(input("Số ngày đi làm: "))
    text = "Nhân viên chuyên cần tốt" if number_work >= 20 else "Cần cải thiện chuyên cần"
    print(f"""
        Thông tin nhân viên:
        Tên: {name}
        Số ngày đi làm: {number_work}
        {text}
    """)
    i += 1
    
