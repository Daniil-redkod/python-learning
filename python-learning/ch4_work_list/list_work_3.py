# Работа с частью списка
# Нарезка списков
players = ['messi', 'ronaldo', 'kaka', 'runi', 'holand']
print(players[0:3])
print(players[1:4])
print(players[:3])
print(players[2:])
print(players[-2:])
print(players[:-1])
print(players[0:4:2])

# Перебор содержимого среза
players = ['messi', 'ronaldo', 'kaka', 'runi', 'holand']
print(f"Это мои любимые игроки:")
for player in players[0:3]:
    print(player.title())

# Копирование списка
team_players = players[:]
print(team_players)

players.append('dembele')
team_players.append('gigs')

print(players)
print(team_players)

# Ошибка копирования списка

pet_1 = ['dog','cat']
pet_2 = pet_1

pet_1.append('snake')
pet_2.append('hamster')

print(pet_1)
print(pet_2)

pet_1.append('cow')

print(pet_1)
print(pet_2)

# Упражнения
# 4.10 Срезы
players1 = ['messi', 'ronaldo', 'kaka', 'runi', 'holand']
print(f"Список игроков - {players1[:]}")
print(f"Первые три пункта в списке - это {players1[:3]}")
print(f"Три пункта из середины списка - это {players1[1:4]}")
print(f"Последние три пункта из списка - это {players1[-3:]}")

# 4.11 Моя пицца, твоя пицца
pizzas = ['Гавайская', 'Фермерская', 'Итальянская']
friend_pizzas = pizzas[:]
pizzas.append('hot')
friend_pizzas.append('spicy')
print(f"Мои пиццы - {pizzas}")
print(f"Пиццы друга - {friend_pizzas}")

for pizza in pizzas:
    print(f"Моя пицца - {pizza}")

for pizza_friend in friend_pizzas:
    print(f"Пицца друга - {pizza_friend}")

for player in players:
    print(f"Мой любимый футболист - {player}")

for team_player in team_players:
    print(f"Любимый футболист друга - {team_player}")