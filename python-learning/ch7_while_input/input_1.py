# input
massage = input("Напиши число: ")
print(massage)

name = input("Напишите Ваше имя: ")
print(f"Здравствуйте, {name.title()}!")

# Объединение несколько строк в одну для переменной
promt = "Мы вместе были на чемпионате мира "
promt += "и болели за Аргентину!"
promt += "\nПобедила Испания? "
name = input(promt)
print(f"Ваш ответ: {name}!")

# Преобразование строки в int
age = input("Сколько тебе лет? ")
age = int(age)
print(age + 10)

# Или можно так
age = int(input("Сколько тебе лет? "))
print(age + 10)

# Проверка роста.py
height = input("Какой у тебя сейчас рост? ")
height = int(height)

if height >= 48:
    print("Вам можно кататься на это горке!")
else:
    print("Вы недостаточного роста.")

# Оператор деления по модулю
# Возвращает остаток от деления
ostatok = 6 % 2
print(ostatok)

ostatok = 5 % 2
print(ostatok)

number = input("Введите число и я скажу Вам четное оно или не четное")
number = int(number)

if number % 2 == 0:
    print("Число четное!")
else:
    print("Число нечетное!")

# Упражнения
# 7.1 Каршеринг
car = input("Какую машину вы бы хотели взять в аренду? ")
print(f"Вы выбрали прекраный автомобиль - {car}!")

# 7.2 Заказ стола
number_of_seats = int(input("На сколько мест Вам нужен столик? "))
if number_of_seats > 8:
    print("Вам придется подождать")
else:
    print("Ваш столик готов!")

# 7.3 Числа, кратные 10
number_10 = int(input("Введите число!"))
if number_10 % 10 == 0:
    print("Число кратно 10")
else:
    print("Число не кратно 10")
