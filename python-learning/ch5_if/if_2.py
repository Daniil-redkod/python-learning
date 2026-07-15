# Простые операторы if
age = 19
if age >= 18:
    print("You are old enouhg to vote!")
    print("Have you registered to vote yet?")

# Операторы if-else
age = 17
if age >= 18:
    print("You are old enouhg to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote")
    print("Please register to vote as soon as you turn 18!")


# Цепочки if-elif-else
age = 5
if age <= 4:
    print("Вход бесплатно")
elif age < 18:
    print("Билет стоит 500 рублей")
else:
    print("Билет стоит 1000 рублей")

age = 70
if age <= 4:
    price = 0
elif age < 18:
    price = 500
elif age >= 65:
    price = 100
else:
    price = 1000

print(f"Билет стоит {price} рублей")

# Тот же код что и выше
age = 70
if age <= 4:
    price = 0
elif age < 18:
    price = 500
elif age < 65:
    price = 500
elif age >= 65:
    price = 100

print(f"Билет стоит {price} рублей")

# Проверка нескольких условий
topings = ['креветка', 'сыр', 'чеснок']
if 'сыр' in topings:
    print("Нужно добавить к заказу сыр")
if 'пеперони' in topings:
    print("Нужно добавить к заказу пеперони")
if 'креветка' in topings:
    print("Нужно добавить к заказу креветка")
print("\nВаша пицца готова\n")

# Упражнения
# 5.3. Цвета пришельцев 1.
alien_color = ('green', 'yellow', 'red')
if 'green' in alien_color:
    print("Вы заработали только что 5 очков!")
if 'black' in alien_color:
    print("Вы заработали только что 7 очков!")

# 5.4. Цвета пришельцев 2.
alien_color = ('green', 'yellow', 'red')
if 'green' in alien_color:
    print("Вы заработали только что 3 очка!")
else:
    print("Вы заработали только что 10 очков!")

alien_color = ('green', 'yellow', 'red')
if 'black' in alien_color:
    print("Вы заработали только что 1 очко!")
else:
    print("Вы заработали только что 12 очков!")

# 5.5. Цвета пришельцев 3.
print("3 версии")
alien_color = ('green', 'yellow', 'red')
if 'black' in alien_color:
    print("Вы заработали только что 3 очка!")
elif 'yellow' in alien_color:
    print("Вы заработали только что 6 очков!")
else:
    print("Вы заработали только что 10 очков!")

alien_color = ('green', 'yellow', 'red')
if 'green' in alien_color:
    print("Вы заработали только что 3 очка!")
elif 'black' in alien_color:
    print("Вы заработали только что 6 очков!")
else:
    print("Вы заработали только что 10 очков!")

alien_color = ('green', 'yellow', 'red')
if 'white' in alien_color:
    print("Вы заработали только что 3 очка!")
elif 'black' in alien_color:
    print("Вы заработали только что 6 очков!")
else:
    print("Вы заработали только что 10 очков!")

# 5.6 Периоды жизни
age = 18

if age < 2:
    age_period = 'младенец'
elif age < 4:
    age_period = 'малыш'
elif age < 13:
    age_period = 'ребенок'
elif age < 18:
    age_period = 'подросток'
elif age < 65:
    age_period = 'взрослый'
else:
    age_period = 'пожилой человек'
print(f"Вы {age_period}")

# 5.7 Любимый фрукт
favorite_fruts = ['банан', 'яблоко', 'апельсин', 'мандарин']
if 'банан' in favorite_fruts:
    print("Вы очень любите бананы")
if 'морковь' in favorite_fruts:
    print("Вы очень любите морковь")
if 'мандарин' in favorite_fruts:
    print("Вы очень любите мандарины")
