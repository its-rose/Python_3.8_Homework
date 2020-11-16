# Задание 1. Напишите функцию, которая будет определять полиндром ли, введенная строка. Если да, то печатать True,
# если нет - False.
# string_ = input('Введите слово палиндром: ')
# if string_ == string_[::-1]:
#     print('True')
# else:
#     print('False')

# Задание 2. Дана строка, в которой встречается одна и та же буква два и более раз.
# Вывести индекс первой и последней буквы. Не используйте циклы в этой задаче.
# string1 = input('Введите текст: ')
# list1 = list(string1)
# q_of_r = string1.count('r')
# print(q_of_r)
# if q_of_r >= 2:
#     print(string1.index('r'))
#     print(string1.rindex('r'))


# Задание 3. Напишите функцию, которая будет суммировать введенные три случайные цифры.
# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))
# num3 = int(input('Введите третье число: '))
# lambda_func = lambda x, y, z: x + y + z
# print(lambda_func(num1, num2, num3))

# Задание 4. Попросить пользователя ввести слова через пробел. Отсортировать слова по кол-ву символов
# и вывести на экран результат.
# text1 = input('Введите несколько слов через пробел: ')
# a = text1.split()
# a.sort(key=len)
# print(a)

# Задание 5. Попросите пользователя ввести букву, если она есть в тексте "Hello World!", напечатать "Hello",
# в противном случае "Bye".
# letter = input('Введите букву: ')
# str_ = 'Hello World!'
# list1 = list(str_)
# list2 = list(str_.swapcase())
# if letter in list1 or letter in list2:
#     print('Hello')
# else:
#     print('Bye')

# Задание 6. Найдите числа кратные 7 и 5 между 1500 и 2700.
# list_ = [i for i in range(1500, 2701)]
# list2 = []
# for i in list_:
#     if i % 5 == 0 or i % 7 == 0:
#         list2.append(i)
# print(list2)

# Задание 7. Напишите программу, которая печатает все числа от 0 до 6, кроме 3 и 6.
# Используйте оператор continue.
# for i in range(0, 7):
#     if i == 3 or i == 6:
#         continue
#     print(i)

# Задание 8. Напишите программу, которая принимает последовательность строк (в нижнем регистре),
# а выводит данные символами в верхнем регистре.
# str_ = input('Введите текст символами в нижнем регистре: ')
# print(str_.upper())

# Задание 9. Напишите программу, которая принимает строку и рассчитывает кол-во цифр и букв.
# str_ = input('Введите текст, состоящий из букв и цифр: ')
# list_ = list(str_)
# list_num = []
# list_alpha = []
# for i in list_:
#     if i == '1' or i == '2' or i == '3' or i == '4' or i == '5' \
#             or i == '6' or i == '7' or i == '8' or i == '9':
#         list_num.append(i)
#         a = len(list_num)
#     else:
#         list_alpha.append(i)
#         x = list_alpha.count(' ')
#         b = len(list_alpha) - x
# print(f'количество цифр {a}, количество букв {b}')

# или
# str_ = input('Введите текст, состоящий из букв и цифр: ')
# list_num = []
# list_alpha = []
# for i in str_:
#     if i.isdigit():
#         list_num.append(i)
#     elif i.isalpha():
#         list_alpha.append(i)
# print(len(list_num))
# print(len(list_alpha))

# Задание 10. Напишите программу, чтобы проверить является ли буква гласной или согласной.
# letter = input('Введите любую букву алфавита: ')
# l = letter.upper()
# if l == 'А' or l == 'Е' or l =='Ё' or l == 'И' or l == 'О' or l == 'У' or l == 'Ы':
#     print(f'{l} - гласная буква')
# elif l == 'Э' or l == 'Ю' or l == 'Я':
#     print(f'{l} - гласная буква')
# else:
#     print(f'{l} - согласная буква')

# Задание 11. Напишите программу, которая считает числа, которые вводит пользователь, пока не будет введено слово 'end'.
# В конце вывести все числа, через запятую, их сумму и среднее значение.
# list_of_num = []
# while True:
#     num = input('Введите число: ')
#     if num != 'exit':
#         list_of_num.append(num)
#         continue
#     elif num == 'exit':
#         break
# a = list(map(int, list_of_num))
# print(f'Вы ввели {a}')
# print(sum(a))
# print(sum(a) / len(a))

# Задание 12. Напишите программу, которая будет запрашивать имя, фамилию, год рождения и страну проживания пользователя.
# Вывести на экран все данные, вместо года рождения указать возраст.
# name = input('Укажите Ваше имя: ')
# last_name = input('Укажите Вашу фамилию: ')
# date_of_b = int(input('Укажите Ваш год рождения: '))
# age = 2020 - date_of_b
# country = input('Укажите Вашу страну проживания: ')
# print(f'Привет, {name} {last_name}. Вам {age} лет. Вы проживаете в {country}.')

# Задание 13. Расположите элементы массива в правильном порядке.
# Используйте конкатенацию и обращение к элементам по индексу.
# yoda = ['on Python', 'programming', 'I like']
# print(yoda[2] + ' ' + yoda[1] + ' ' + yoda[0])

# Задание 14. Запросите оценки для 4-х учеников. В конце выведите среднюю оценку для всей группы,
# округленную в большую сторону (оценка ср арифметическая).
# import math
# mark1 = int(input('Enter mark for Bill: '))
# mark2 = int(input('Enter mark for Jane: '))
# mark3 = int(input('Enter mark for John: '))
# mark4 = int(input('Enter mark for Mary: '))
# marks = {'Bill': mark1, 'Jane': mark2, 'John': mark3, 'Mary': mark4}
# print(marks)
# sum_ = marks['Bill'] + marks['Jane'] + marks['John'] + marks['Mary']
# av_mark = math.ceil(sum_ / 4)
# print(f'Average mark: {av_mark}')
