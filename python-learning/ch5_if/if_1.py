# cars
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    elif car == 'audi':
        print(car.lower())
    else:
        print(car.title())

# сравнение
car1 = 'Audi'
sravnenie1 = car1 == 'audi'
sravnenie2 = car1.lower() == 'audi'
print(f"Audi равно audi? Ответ: {sravnenie1}")
print(f"audi равно audi? Ответ: {sravnenie2}")

# проверка неравенства
car1 = 'Audi'
sravnenie1 = car1 != 'audi'
sravnenie2 = car1.lower() != 'audi'
print(f"Audi не равно audi? Ответ: {sravnenie1}")
print(f"audi не равно audi? Ответ: {sravnenie2}")

# проверка неравенства
toping = "Грибы"
if toping != "Анчоус":
    print("Закажите Анчоус!")


# Мини программа угадай число (сравнение)
"""
answer = int(input())

if answer != 17:
    print(f"Вы выбрали {answer}! Не верно, выбери другое число")
else:
    print(f"Вы выбрали {answer}! Поздравляю, вы угадали!")
"""

# age = 19
# age <= 18
# age >= 18
# age < 18
# age > 18

# Проверка нескольких условий
# and
age_0 = 22
age_1 = 18
print((age_0 > 10) and (age_1 <= 22))
print(age_0 == 10 and age_1 <= 22)

# or
age_0 = 22
age_1 = 18
print((age_0 > 10) or (age_1 <= 22))
print(age_0 == 10 or age_1 <= 22)

# Проверка в списке есть ли
topings = ['mushrooms', 'onios', 'pineapple']
print("Проверка в списке mushrooms:")
print('mushrooms' in topings)
print("Проверка в списке peperoni:")
print('peperoni' in topings)

# Проверка в списке нет ли

banned_users = ['andrew', 'fred', 'max']
user = 'marina'
if user not in banned_users:
    print(f"Этот пользователь {user.title()} не в бане")

# Упражнения
# 5.1 Проверка условий
car = 'subaru'
print(f"car = {car}")
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False")
print(car == 'audi')
