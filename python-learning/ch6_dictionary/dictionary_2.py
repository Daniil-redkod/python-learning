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
