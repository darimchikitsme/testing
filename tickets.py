tickets = int(input("Акция - при покупке более 3 билетов действует скидка 10 % \nВведите количество билетов: "))
total_price = 0

for i in range(tickets):
    age = int(input(f"Введите возраст посетителя: "))
    if age < 18:
        total_price += 0
    elif age < 25:
        total_price += 990
    else:
        total_price += 1390

if tickets > 3:
    total_price *= 0.9

print(f"Сумма к оплате: {total_price} руб.")
