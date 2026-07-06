# Первый элемент из списка
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
massege = f'My first bicycle was a {bicycles[0].title()}'
print(massege)

# Работа со списком
names = ['dan', 'anton', 'denis']
print(names[0].title())
print(names[1].title())
print(names[2].title())

print(f"Привет, {names[0].title()}!")
print(f"Привет, {names[1].title()}!")
print(f"Привет, {names[2].title()}!")

car_names = ['bmv', 'audi', 'kia']
print(f"Я хочу купить {car_names[0].upper()}!")
print(f"Я хочу купить {car_names[1].upper()}!")
print(f"Я хочу купить {car_names[2].upper()}!")

# Изменение, добавление и удаление элементов в списке
# Изменение
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# Добавление
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

team = []
team.append('arsenal')
team.append('psg')
team.append('Real Madrid')
print(team)

# Вставка insert
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(2, 'bmw')
print(motorcycles)

team.insert(0, 'zenit')
print(team)

# Удаление
# опепратор del
del team[0]
print(team)

del team[2]
print(team)

# опепратор pop
print(motorcycles)
moto = motorcycles.pop()
print(motorcycles)
print(moto)

last_car = car_names.pop()
print(f"Последний проданный автомобиль это {last_car.upper()}.")

# pop произвольный элемент из списка
moto = motorcycles.pop(0)
print(motorcycles)
print(moto)

print(car_names)
first_car = car_names.pop(0)
print(f"Первый проданный автомобиль это {first_car.upper()}.")

# Удаление по названию
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.remove('honda')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nО, {too_expensive.title()} это слишком дорого для меня.")

# Упражнения
dinner = ['Messi', 'ronaldo', 'pele']
print(f"Приглашаю Вас на ужин дорогой, {dinner[0]}!")
print(f"Приглашаю Вас на ужин дорогой, {dinner[1]}!")
print(f"Приглашаю Вас на ужин дорогой, {dinner[2]}!")

print(f"К сожалению на ужин не сможет придти {dinner[2]}.")
del dinner[2]
dinner.append('maradona')
print(f"Приглашаю Вас на ужин дорогой, {dinner[2]}!")
print(f'Список приглашенных: {dinner}')

dinner.insert(0, 'kaka')
dinner.insert(2, 'runi')
dinner.append('pirlo')
print(f"Приглашаю Вас на ужин дорогой, {dinner[0]}!")
print(f"Приглашаю Вас на ужин дорогой, {dinner[2]}!")
print(f"Приглашаю Вас на ужин дорогой, {dinner[5]}!")
print(f'Список приглашенных: {dinner}')

print(f"К сожалению на ужин можно придти только двум людям.")
minus_1 = dinner.pop()
print(f"К сожалению ужин отменяется дорогой, {minus_1}.")
minus_2 = dinner.pop()
print(f"К сожалению ужин отменяется дорогой, {minus_2}.")
minus_3 = dinner.pop()
print(f"К сожалению ужин отменяется дорогой, {minus_3}.")
minus_4 = dinner.pop()
print(f"К сожалению ужин отменяется дорогой, {minus_4}.")
print(f'Список приглашенных: {dinner}')

print(f"Ужин состоится дорогой, {dinner[0]}!")
print(f"Ужин состоится дорогой, {dinner[1]}!")

del dinner [1]
del dinner [0]
print(f'Список оставшихся: {dinner}')