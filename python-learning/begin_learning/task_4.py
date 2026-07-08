oklad = (int(input("Введите оклад: ")))
premiya = (int(input("Введите процент премии: ")))
print(f"Ваша зарплата состовляет: {(oklad + (oklad * (premiya / 100))):.0f}")