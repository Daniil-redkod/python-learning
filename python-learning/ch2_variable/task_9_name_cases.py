# Использование переменной в выводе сообщения
name = "Эрик"
massege = f"Здравствуйте, {name}, не хотите сегодня пообедать?"
print(massege)

# Изменение регистра
first_name = 'dan'
last_name = 'Petrov'
full_name = f'{first_name} {last_name}'
registr1 = full_name.title()
registr2 = full_name.upper()
registr3 = full_name.lower()
print(f'\n{registr1}, \n{registr2}, \n{registr3}.')

# Удаление лишних пробелов в начале и в конце строки
name = ' dan '
print(f'!{name.rstrip()}!')
print(f'!{name.lstrip()}!')
print(f'!{name.strip()}!')
name = name.strip()
print(f'\n\t!{name}!')

# Удаление из текста расширения файла
file_name = 'python_notes.txt'
file_name = file_name.removesuffix('.txt')
print(file_name)