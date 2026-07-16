# Использование операторов if со списками
# Проверка специальных значений
topings = ['креветка', 'сыр', 'чеснок']
for toping in topings:
    print(f"Нужно добавить {toping}")
print("\nВаша пицца готова\n")

topings = ['креветка', 'сыр', 'чеснок']
for toping in topings:
    if toping == "чеснок":
        print("Извините, чеснока нет в нашем ресторане")
    else:
        print(f"Нужно добавить {toping}")
print("\nВаша пицца готова\n")

# Если список пуст
topings = []
if topings:
    for toping in topings:
        if toping == "чеснок":
            print("Извините, чеснока нет в нашем ресторане")
        else:
            print(f"Нужно добавить {toping}")
else:
    print("А вы добавили топинги для пиццы?")

# Множественные списки
klient_topings = ['картошка фри', 'сыр', 'бекон', 'анчоус']
restoran_topings = ['креветка', 'сыр', 'чеснок', 'анчоус']

for toping in klient_topings:
    if toping not in restoran_topings:
        print(f"Извините, в нашем меню нет {toping} "
              f"\nесть только такие топинги {restoran_topings}")
    else:
        print(f"Нужно добавить {toping}")
print("\nВаша пицца готова\n")

# Упражнения
# 5.8 Здравствуйте, админ!

users = ['admin', 'piter', 'dan', 'alex', 'jon']

for user in users:
    if user == 'admin':
        print("Hello administrator!")
    else:
        print(f"Hello {user}!")

# 5.9 Нет пользователей
users = []

if users:
    for user in users:
        if user == 'admin':
            print("Hello administrator!")
        else:
            print(f"Hello {user}!")
else:
    print("No users")

# 5.10 Проверка имен пользователей

current_users = ['admin', 'piter', 'dan', 'alex', 'jon']
new_users = ['mikl', 'DaN', 'GORDON', 'stas', 'Alex']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"{new_user} - Имя занято")
    else:
        print(f"{new_user} - Имя доступно")

# 5.11 Порядковые числительные

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
for number in numbers:
    if number == '1':
        print(f"{number}st")
    elif number == '2':
        print(f"{number}nd")
    elif number == '3':
        print(f"{number}rd")
    else:
        print(f"{number}th")
