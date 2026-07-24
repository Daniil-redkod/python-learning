# Цикл while
"""
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

    
promt = "\nСкажи мне и я завершу работу:"
promt += "\nНапиши 'Выход' и работа программы завершится. "

massage = ""
while massage != 'Выход':
    massage = input(promt)

    if massage != 'Выход':
        print(massage)

# Флаги
promt = "\nСкажи мне и я завершу работу:"
promt += "\nНапиши 'Выход' и работа программы завершится. "

active = True
massage = ""
while active:
    massage = input(promt)

    if massage == 'Выход':
        active = False
    else:
        print(massage)

# Оператор break и выход из цикла
promt = "\nКакой город тебе нравится?:"
promt += "\nНапиши 'Выход' и работа программы завершится. "

while True:
    city = input(promt)

    if city == 'Выход':
        break
    else:
        print(f"Я люблю этот город {city}!")

# Оператор continue и продолжение цикла
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

# Предотвращение зацикливания
x = 1
while x <= 5:
    print(x)
    x += 1

# Упражнения
# 7.4 Начинки для пиццы
promt = "Напишие название начинки для пиццы, которую хотите добавить в заказ"
promt += "Для выхода напишите 'q': "

while True:
    zakaz = input(promt)

    if zakaz == "q":
        break
    else:
        print(f"Ваша начинка - {zakaz} доьавлена в заказ!")

# 7.5 Билеты в кино
while True:
    sale_ticket = int(input("Назовите свой возраст: "))
    if sale_ticket < 3:
        ticket = 'Бесплатно'
        break
    elif sale_ticket >= 3 and sale_ticket <= 12:
        ticket = '10$'
        break
    else:
        ticket = '15$'
        break
print(f"Ваш билет стоить будет: {ticket}")


# 7.6 Три выхода
promt = "Напишие название начинки для пиццы, которую хотите добавить в заказ"
promt += "\nДля завершения заказа напишите 'pizza': "
promt += "\nДля выхода напишите 'q': "

active = True
while active:
    zakaz = input(promt)

    if zakaz == "q":
        break
    elif zakaz == "pizza":
        active = False
    else:
        print(f"Ваша начинка - {zakaz} доьавлена в заказ!")
        break
"""
# 7.7 Бесконечвный цикл
number = 11
while number >= 10:
    print(number)
