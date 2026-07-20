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
