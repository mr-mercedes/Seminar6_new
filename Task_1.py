# Задача 1. Дано натуральное число N. Найдите значение выражения:N + NN + NNN. N может быть любой длины.
# N = 132: 132 + 132132 + 132132132 = 132264396

user_input = input("Введите число: ")
result = int(user_input) + int(user_input * 2) + int(user_input * 3)
print(result)
