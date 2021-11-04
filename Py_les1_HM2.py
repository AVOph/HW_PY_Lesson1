sec_input = int(input("Введите количество секунд:"))

hours = sec_input//3600
minutes = sec_input%3600//60
seconds = sec_input%3600%60
print(f"{hours:02}:{minutes:02}:{seconds:02}")
