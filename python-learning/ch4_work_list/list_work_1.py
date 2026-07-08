# Перебор всего списка
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# Более сложные действия в циклах for
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print(f"Thank you, everyone. That was a great magic show!\n")

# Упражнения
# 4.1 Пицца
pizzas = ['Гавайская', 'Фермерская', 'Итальянская']
for pizza in pizzas:
    print(f"Эта пицца: {pizza} - вкусная")
print(f"\nЯ очень люолю пиццу!")

# 4.2 Животные
home_animals = ['Cat', 'Dog', 'hamster']
for home_animal in home_animals:
    print(home_animal)

home_animals = ['Cat', 'Dog', 'hamster']
for home_animal in home_animals:
    print(f"A {home_animal.title()} is a pet")
print(f"\nThey're great pets!\n") 

