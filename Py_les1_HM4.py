input_num = int(input("Введите любое целое число :"))

num_max = 0
while input_num != 0 :
    end_num = input_num%10
    input_num = input_num//10
    if end_num > num_max :
        num_max = end_num
print(f"Самая большая цифра {num_max}")
