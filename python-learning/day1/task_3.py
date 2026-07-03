print("Какой у тебя рост?")
height = input()
print("Какой у тебя вес?")
weight = input()
imt = int(weight) / ((int(height) / 100) ** 2)
print("Индекс массы тела: " + str(imt))

#Правильный код для расчета индекса массы тела (ИМТ) выглядит следующим образом:

height2 = float(input("Введите ваш рост в см: "))
weight2 = float(input("Введите ваш вес в кг: "))
imt2 = weight2 / ((height2 / 100) ** 2)
print(f"Ваш индекс массы тела (ИМТ) составляет: {imt2:.2f}")


