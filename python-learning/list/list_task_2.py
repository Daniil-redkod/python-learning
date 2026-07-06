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