print("Как тебя зовут?")
name = input()
print("Привет, " + name + "!")
while True:
    print("Сколько тебе лет?")
    try:
        age = int(input())
        break
    except ValueError:
        print("Пожалуйста, введите корректное число.")
print("О, тебе " + str(age) + " лет! Это замечательно!")
age1 = age + 1
print("А через год тебе будет " + str(age1) + " лет!")