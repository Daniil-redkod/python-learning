# Использование операторов if со списками
# Проверка специальных значений
topings = ['креветка', 'сыр', 'чеснок']
for toping in topings:
    print(f"Нужно добавить {toping}")
print("\nВаша пицца готова\n")

topings = ['креветка', 'сыр', 'чеснок']
for toping in topings:
    if toping == "чеснок":
        print("Извините, чеснока нет в нашем ресторане")
    else:
        print(f"Нужно добавить {toping}")
print("\nВаша пицца готова\n")

# Если список пуст
topings = []
if topings:
    for toping in topings:
        if toping == "чеснок":
            print("Извините, чеснока нет в нашем ресторане")
        else:
            print(f"Нужно добавить {toping}")
else:
    print("А вы добавили топинги для пиццы?")

# Множественные списки
klient_topings = ['картошка фри', 'сыр', 'бекон', 'анчоус']
restoran_topings = ['креветка', 'сыр', 'чеснок', 'анчоус']

for toping in klient_topings:
    if toping not in restoran_topings:
        print(f"Извините, в нашем меню нет {toping} "
              f"\nесть только такие топинги {restoran_topings}")
    else:
        print(f"Нужно добавить {toping}")
print("\nВаша пицца готова\n")
