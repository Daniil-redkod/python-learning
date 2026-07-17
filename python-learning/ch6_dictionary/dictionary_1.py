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

# Словарь с однотипными объектами
favorite_languages = {
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
alien_0 = {'color': 'green', 'points': '5', 'speed': '5'}
speed_value = alien_0.get('speed', 'No speed value assigned')
print(speed_value)
print(alien_0['speed'])

# Упражнения
# 6.1 Персона
person_1 = {
        'first_name': 'Maksim',
        'last_name': 'Bykov',
        'age': 18,
        'city': 'Moscow',
        }

print(person_1['first_name'])
print(person_1['last_name'])
print(person_1['age'])
print(person_1['city'])

# 6.2 Любимые чиса

love_numbers = {
            'max': 3,
            'anton': 5,
            'denis': 6,
            'stepan': 10,
            'peter': 11,
            }

print(f"Любимое число Макса: {love_numbers['max']}")
print(f"Любимое число Антона: {love_numbers['anton']}")
print(f"Любимое число Дениса: {love_numbers['denis']}")
print(f"Любимое число Степы: {love_numbers['stepan']}")
print(f"Любимое число Пети: {love_numbers['peter']}")

love_numbers = {
            'макс': 3,
            'Антон': 5,
            'ДениС': 6,
            'Степа': 10,
            'Петя': 11,
            }

for name, number in love_numbers.items():
    print(f"{name.title()} любит число: {number}!")

# 6.3 Глоссарий.

glossari = {
        'Пайтон': 'это высокоуровневый язык программирования',
        'Переменная': 'это имя (ярлык), которое '
        'ссылается на область памяти, где хранится значение',
        'Словарь': 'это структура данных для хранения '
        'взаимосвязанной информации',
        }

for termin, definition in glossari.items():
    print(f"\n{termin} - \n{definition}")

# Перебор словая
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermin',
    }

for key, value in user_0.items():
    print(f"\nКлюч: {key}")
    print(f"\nЗначение: {value}")

# Перебор всех ключей в словаре
favorite_languages = {
                'jen': 'python',
                'sarah': 'c',
                'edward': 'rust',
                'phil': 'python',
                }

for name in favorite_languages.keys():
    # for name in favorite_languages(): Тот же код, работает по умолчанию
    print(name.title())

favorite_languages = {
                'jen': 'python',
                'sarah': 'c',
                'edward': 'rust',
                'phil': 'python',
                }

friends = ['sarah', 'phil']

for name in favorite_languages.keys():
    print(f"Hi, {name.title()}!")
    if name in friends:
        languages = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {languages}!")


if 'erin' not in favorite_languages.keys():
    print("\nErin не учавствовал в опросе")

# Перебор ключей словая в определенном порядке
favorite_languages = {
                'jen': 'python',
                'sarah': 'c',
                'edward': 'rust',
                'phil': 'python',
                }

for name in sorted(favorite_languages.keys()):
    print(f"Hi, {name.title()}!")

# Перебор всех значений в словаре
favorite_languages = {
                'jen': 'python',
                'sarah': 'c',
                'edward': 'rust',
                'phil': 'python',
                }
print("Список ответов в опросе по языкам")
for language in favorite_languages.values():
    print(language.title())

# Убрать дубикаты значений функцией set()
favorite_languages = {
                'jen': 'python',
                'sarah': 'c',
                'edward': 'rust',
                'phil': 'python',
                }
print("Список ответов в опросе по языкам без дубликатов")
for language in set(favorite_languages.values()):
    print(language.title())

# множество
language = {'python', 'c', 'rust', 'python'}
print(language)

# 6.4 Глоссарий 2 сделано в 6.3

# 6.5 Реки
river_countries = {
    'Нил':  'Египет',
    'Елена': 'Россия',
    'Амазонка': 'Африка',
    }

for river, country in river_countries.items():
    print(f"{river} протекает через {country}.")

for river in river_countries.keys():
    print(river)

for country in river_countries.values():
    print(country)

# 6.6 Опрос.
favorite_languages = {
                'jen': 'python',
                'sarah': 'c',
                'edward': 'rust',
                'phil': 'python',
                }

people_survey = ['jen', 'sarah', 'edward', 'phil', 'max', 'tomas', 'jim']
for name in people_survey:
    if name in favorite_languages:
        print(f"{name.title()} спасибо за участие в опросе!")
    else:
        print(f"{name.title()} пожауйста, примите участие в опросе.")
