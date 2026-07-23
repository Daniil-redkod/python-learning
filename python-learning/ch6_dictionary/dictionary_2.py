# Вложение данных
# Список словарей
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'red', 'points': 10}
alien_2 = {'color': 'blue', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
print(aliens)

for alien in aliens:
    print(alien)

aliens = []

# Создание 30 зеленых пришельцев
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 0, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print("...")

print(f"Обчее количество зеленых пришельцев = {len(aliens)}")

# Изменение 3 пришельцев
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

for alien in aliens[:5]:
    print(alien)

# Список в словаре
# pizza.py
# Сохранение информации о заказанной пиццы
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

# Описание заказа
print(f"You ordered a {pizza['crust']} - crust pizza "
      "with the following toppings")

for toping in pizza['toppings']:
    print(f"\t{toping}")

# Пример с языками

favorite_languages = {
                'jen': ['python', 'c'],
                'sarah': ['c'],
                'edward': ['rust', 'c#'],
                'phil': ['python', 'java'],
                }

friends = ['bob', 'anton', 'jen', 'sarah', 'edward', 'phil']


for name in friends:
    if name in favorite_languages:
        if len(favorite_languages[name]) == 1:
            print(f"{name} - любит этот язык программирования ")
        else:
            print(f"{name} - любит эти языки программирования ")
        for language in favorite_languages[name]:
            print(f"\t{language}")
    else:
        print(f"{name} - необходимо пройти опрос")

# Вложение словарей в словарь
# many_users.py
users = {
    'maximus': {
        'first': 'max',
        'last': 'popov',
        'location': 'moscow',
        },

    'sis01': {
        'first': 'sis',
        'last': 'zola',
        'location': 'paris',
        },
}

for user_name, user_info in users.items():
    print(user_name)
    for first, name in user_info.items():
        print(f"\t{first} - {name}")

# Второй вариант
users = {
    'maximus': {
        'first': 'max',
        'last': 'popov',
        'location': 'moscow',
        },

    'sis01': {
        'first': 'sis',
        'last': 'zola',
        'location': 'paris',
        },
}

for user_name, user_info in users.items():
    print(f"\nUsername: {user_name}")
    fullname = f"{user_info['first']} {user_info['last']}"
    location = f"{user_info['location']}"

    print(f"\tПолное имя: {fullname.title()}")
    print(f"\tЛокация: {location.title()}")

# Упражнения
# 6.7 Люди
person_1 = {
        'first_name': 'Maksim',
        'last_name': 'Bykov',
        'age': 18,
        'city': 'Moscow',
        }

person_2 = {
        'first_name': 'Andrew',
        'last_name': 'Alekseev',
        'age': 22,
        'city': 'Saint-Petersburg',
        }

person_3 = {
        'first_name': 'Anton',
        'last_name': 'Karpov',
        'age': 44,
        'city': 'Tagil',
        }

peoples = []

peoples.append(person_1)
peoples.append(person_2)
peoples.append(person_3)

for people in peoples:
    print("Человек в списке:")
    for key, value in people.items():
        print(f"{key} - {value}")
    print()

# 6.8 Домашние животные
pets = []

chaki = {
    'chaki': {
            'type_of_animal': 'cat',
            'owner': 'dan',
            }
    }

pity = {
    'pity': {
            'type_of_animal': 'dog',
            'owner': 'max',
            }
    }

homa = {
    'homa':{
            'type_of_animal': 'humster',
            'owner': 'stas',
            }
    }

pets.append(chaki)
pets.append(pity)
pets.append(homa)

print("Информация о домашних животных:\n")
for pet in pets:
    for nickname in pet:
        print(f"{nickname}")
        for key, value in pet[nickname].items():
            print(f"\t{key} - {value}")
    print()

# 6.9 Любимые места
favorite_places = {
    'piramida': 'Пирамида - очень красивое место в Каире',
    'efel': 'Эйфелева баня - замечательное место в Париже',
    'peterhof': 'Петергоф - город с фонтанами в Санкт-Петербурге'
    }

person_1 = {
        'first_name': 'Maksim',
        'last_name': 'Bykov',
        'age': 18,
        'city': 'Moscow',
        }

person_2 = {
        'first_name': 'Andrew',
        'last_name': 'Alekseev',
        'age': 22,
        'city': 'Saint-Petersburg',
        }

person_3 = {
        'first_name': 'Anton',
        'last_name': 'Karpov',
        'age': 44,
        'city': 'Tagil',
        }

peoples = {
        'p1_like_places': {
            'person_1': person_1['first_name'],
            'like_place_1': favorite_places['efel'],
            },
        'p2_like_places': {
            'person_2': person_2['first_name'],
            'like_place_1': favorite_places['efel'],
            'like_place_2': favorite_places['piramida'],
            },
        'p3_like_places': {
            'person_3': person_3['first_name'],
            'like_place_1': favorite_places['efel'],
            'like_place_2': favorite_places['peterhof'],
            'like_place_3': favorite_places['piramida'],
            }
        }

print("Любимые места моих друзей:")
for people in peoples:
    print()
    print(f"--- {people.upper()} ---") 
    for key, value in peoples[people].items():
        print(f"{key} - {value}")

print()
for key, value in favorite_places.items():
    print(f"{key} - {value}")


# 6.10 Любимые числа
love_numbers = {
            'макс': [3, 4],
            'Антон': [5, 7, 8],
            'ДениС': [6],
            'Степа': [10, 12],
            'Петя': [11, 15],
            }

for name, number in love_numbers.items():
    if len(number) == 1:
        print(f"{name.title()} любит число: {number}!")
    else:
        print(f"{name.title()} любит числа: {number}!")

# 6.11 Города
cities = {
    'москва': {'страна': 'россия',
               'численность': '13 млн',
               'памятник': 'мавзолей ленина',
               },
    'варшава': {'страна': 'польша',
                'численность': '2 млн',
                'памятник': 'варшавская русалочка',
                },
    'париж': {'страна': 'франция',
              'численность': '12 млн',
              'памятник': 'эйфелева башня',
              },
    }
print("\nЛюбимые места:\n")
for city in cities:
    print(f"Город - {city.title()}")
    for key, value in cities[city].items():
        print(f"\t{key.title()} - {value.title()}")
    print()

# 6.12 Расширение
# Словарь словарей
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'red', 'points': 10}
alien_2 = {'color': 'blue', 'points': 15}

aliens = {
    'Пришелец № 1': alien_0,
    'Пришелец № 2': alien_1,
    'Пришелец № 3': alien_2
    }

for key, value in aliens.items():
    print(f"{key}")
    for k, v in value.items():
        print(f"\t{k} - {v}")
    print()
