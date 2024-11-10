first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Генераторная сборка для first_result
first_result = (abs(len(f) - len(s)) for f, s in zip(first, second) if len(f) != len(s))

# Генераторная сборка для second_result
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

# Проверка вывода
print(list(first_result))   # Ожидаемый вывод: [1, 2]
print(list(second_result))   # Ожидаемый вывод: [False, False, True]
