# Задание 1. Выведите все элементы списка которые меньше 5.
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in a:
#     if i < 5:
#         print(i)

# Задание 2. Нужно вернуть список который состоит из элементов, общих для этих двух списков.
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# for i in a and b:
#     if i in a and i in b:
#         print(i)

# Задание 3. Напишите программу для слияния нескольких словарей в один.
# dict1 = {'Mersedes': '221', 'BMW': '750i', 'Subaru': 'impreza'}
# dict2 = {'lenovo': 'yoga', 'macbook': 'pro', 'asus': 'zephyrus'}
# dict3 = {'name': 'John', 'last name': 'Snow'}
# dict1.update(dict2)
# dict1.update(dict3)
# print(dict1)

# Задание 4. Напишите программу которая выводит чётные числа из заданного списка и останавливается
# если встречает число 237.
# numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918,
#            237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217]
# for i in numbers:
#     if i % 2 == 0:
#         print(i, end=' ')
#     elif i == 237:
#         break

# Задание 5. Пользователь вводит два числа не равных друг другу. Выведите все числа которые находятся между ними,
# включая сами числа.
# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число (число не должно быть < первого): '))
# list_ = [i for i in range (num1, num2 + 1)]
# print(list_)

# Задание 6. Пользователь вводит 2 числа. Выведите все квадраты чисел, начиная с наименьшего, которые меньше,
# чем наибольшее число.
# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число (число не должно быть < первого): '))
# list_ = [i ** 2 for i in range (num1, num2 + 1)]
# for i in list_:
#     if i < num2:
#         print(i, end=' ')

# Задание 7. Используя цикл, посчитайте кол-во четных и нечетных чисел.
# nums_ = [1, 2, 6, 3, 9, 2, 11, 20, 16, 7, 8]
# even = 0
# odd = 0
# for i in nums_:
#     if i % 2 == 0:
#         even = even + 1
#     else:
#         odd = odd + 1
# print(f'четных чисел = {even}, нечетных = {odd}')

# Задание 8. Программа для постороения шаблона из цифр от 1 до 9.
# n = 9
# for i in range (n + 1):
#     for ii in range (i):
#         print(i, end='')
#     print('\r')

# Задание 9. Написать программу для написания таблицы умножения на введеное число от 1-10.
# num_ = int(input('Введите любое число от 1-10: '))
# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in list_:
#     print(f'{num_} * {i} = {num_ * i}')

# Задание 10.Вывести на экран ряд натуральных чисел от минимума до максимума с шагом.
# num1 = int(input('Введите минимальное число: '))
# num2 = int(input('Введите максимальное число: '))
# step = int(input('Введите шаг: '))
# for i in range(num1, num2 + 1, step):
#     print(i, end=' ')

# Задание 11. Вывести на экран столько цифр ряда Фибоначчи, сколько укажет пользователь.
# n = int(input('Введите кол-во чисел ряда Фибоначчи: '))
# fib1 = fib2 = 1
# if n < 2:
#     quit()
# print(fib1, end=' ')
# print(fib2, end=' ')
# for i in range(2, n):
#     fib1, fib2 = fib2, fib1 + fib2
#     print(fib2, end=' ')
# print()

# Задание 12.Вычислить факториал введенного числа.
# num_ = int(input('Введите число: '))
# import time
# def factorial(num_):
#     if num_ == 0:
#         return 1
#     else:
#         time.sleep(1)
#         print(num_)
#         print(f'{num_} * factorial({num_} - 1)')
#         return num_ * factorial(num_ - 1)
# print(factorial(num_))