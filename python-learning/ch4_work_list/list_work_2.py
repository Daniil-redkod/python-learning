# Создание числовых списков
for value in range(1,6):
    print(value)

print(f' ')

for value in range(6):
    print(value)

print(f' ')

numbers = list(range(1,6))
print(numbers)

print(f' ')

# Список четных чисел от 1 до 10
even_numbers = list(range(2,11,2))
print(even_numbers)

print(f' ')

# Список нечетных чисел от 1 до 10
even_numbers = list(range(1,11,2))
print(even_numbers)

# Список квадратов всех целых чисел от 1 до 10
even_numbers = list(range(1,11))
squares = []
for even_number in even_numbers:
    number_v_kvadrate = even_number * even_number
    squares.append(number_v_kvadrate)
print(squares)

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

squares = []
for value in range(1,11):
    squares.append(value ** 2)
print(squares)

# Простая статистика с числами
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

# Генератор списков
squares = [value ** 2 for value in range(1,11)]
print(squares)

# Нечетные числа от 1 до 11 
odd_numbers = [f"{value/3:.2f}" for value in range(1,11,2)]
print(odd_numbers)

odd_numbers = [round(value/3,2) for value in range(1,11,2)]
print(odd_numbers)

# Упражнения
# 4.3 Считаем до 20
numbers_20 = range(1,21)
for number in numbers_20:
    print(number)

# 4.4 Миллион
# numbers_1_000_000 = range(1,1000001)
# for number in numbers_1_000_000:
    # print(number)

# 4.5 Суммирование миллиона чисел
numbers_1_000_000 = range(1,1000001)
print(min(numbers_1_000_000))
print(max(numbers_1_000_000))
print(sum(numbers_1_000_000))

# 4.6 Нечетные числа
numbers_20 = range(1,21,2)
for number in numbers_20:
    print(number)

# 4.7 Тройки
numbers_30 = range(3,31,3)
for number in numbers_30:
    print(number)

# 4.8 Кубы
kub = []
for value in range(1,11):
    kub.append(value**3)
print(kub)

# 4.9 Генератор кубов
kub = [value**3 for value in range(1,11)]
print(kub)