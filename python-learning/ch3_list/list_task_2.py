# Упорядочение списка
cars = ['bmw', 'audi', 'subaru', 'toyota']
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'subaru', 'toyota']
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'subaru', 'toyota']
print("\nОригинальный список")
print(cars)
print("\nВременно отсортированный список")
print(sorted(cars))
print("\nОригинальный список сохранился")
print(cars)

cars = ['bmw', 'audi', 'subaru', 'toyota']
print("\nОригинальный список")
print(cars)
print("\nВременно отсортированный список в обратном порядке")
print(sorted(cars, reverse=True))
print("\nОригинальный список сохранился")
print(cars)

# Вывод списка в обратном порядке
cars = ['bmw', 'audi', 'subaru', 'toyota']
cars.reverse()
print(cars)

# Определение длины списка
cars = ['bmw', 'audi', 'subaru', 'toyota']
print(len(cars))

# Упражнения

# 3.8 Повидать мир
country = ['china', 'bali', 'italy', 'usa', 'brazil']
print(country)

print(sorted(country))
print(country)

print(sorted(country, reverse=True))
print(country)

country.reverse()
print(country)

country.reverse()
print(country)

country.sort()
print(country)

country.sort(reverse=True)
print(country)

# 3.9 Количество гостей
# Выполнено в list_task_1

# 3.10 Все функции
games = ['gta6', 'fortnite', 'fifa', 'dota', 'cs2']

games.append('heroes7')
print(games)

games.insert(4, 'nfs')
print(games)

print(sorted(games))
print(games)

games.sort()
print(games)

games.reverse()
print(games)

del games[6]
print(games)

games.remove('dota')
print(games)

game_my = games.pop(1)
print(game_my)

print(games[-1].title())

print(games)
print(len(games))