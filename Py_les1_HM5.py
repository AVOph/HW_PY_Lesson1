proceed = int(input("Укажите выручку :"))
cost = int(input("Укажите издержки:"))
people = int(input("Укажите численность персонала :"))

if proceed < cost:
    print("Фирма работет в убыток!")
elif proceed > cost:
    profit = ((proceed - cost) / proceed) * 100
    profit_for_people = (proceed - cost) / people
    print(f"Ваша фирма работает с прибылью. Рентабельность : {profit} % . Прибыль фирмы на 1 сотрудника {profit_for_people}")
else :
    print("Прибыль отсутствует =(")
