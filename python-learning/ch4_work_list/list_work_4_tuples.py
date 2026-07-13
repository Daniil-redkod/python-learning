# Кортежи
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Ошибка
# dimensions[0] = 250
print(dimensions)

my_t = (3,)
print(my_t)

# Перебор всех значений в кортеже
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

# Замена кортежа
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# Упражнения
# 4.13 Шведский стол
menu_all = ('olivie', 'kefir', 'banan', 'cezar', 'pasta')
for menu_one in menu_all:
    print(menu_one)

# menu_all[0] = ('no')

menu_new = ('krab', 'kefir', 'apple', 'cezar', 'pasta')
for menu_one in menu_new:
    print(f"Новое блюдо - {menu_one}")
