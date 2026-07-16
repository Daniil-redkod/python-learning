# Простой словарь
alien_0 = {'color': 'green', 'points': '5'}
print(alien_0['color'])
print(alien_0['points'])

# Добавление новых пар ключ-значение в словарь
alien_0 = {'color': 'green', 'points': '5'}
alien_0['x_position'] = '0'
alien_0['y_position'] = '25'
print(alien_0)

# Создание пустого словаря
alien_0 = {}
alien_0['x_position'] = '0'
alien_0['y_position'] = '25'
print(alien_0)

# Изменение значений в словаре
alien_0 = {'color': 'green', 'points': '5'}
print(alien_0['color'])
alien_0['color'] = 'red'
print(alien_0['color'])

# Отслеживание позиции
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# Пришелец смещается вправо.
# Вычесляем велечину смещения на основании текущей скорости.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # Пришелец двигается быстро.
    x_increment = 3

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

alien_0['speed'] = 'fast'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # Пришелец двигается быстро.
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")
print(alien_0)

# Удаление пар "Ключ - значение"
alien_0 = {'color': 'green', 'points': '5'}
del alien_0['points']
print(alien_0)

# Словарь с однотипным 
favorite_languages ={
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

languages = favorite_languages['sarah'].title()
print(f"Sarah's favorite languages is {languages}.")

# Обращение к значениям методом get()
# Ошибка
# alien_0 = {'color': 'green', 'points': '5'}
# print(alien_0['speed'])

# Обращение к значениям методом get без второго аргумента()
alien_0 = {'color': 'green', 'points': '5'}
speed_value = alien_0.get('speed')
print(speed_value)

# Обращение к значениям методом get()
alien_0 = {'color': 'green', 'points': '5'}
speed_value = alien_0.get('speed', 'No speed value assigned')
print(speed_value)
