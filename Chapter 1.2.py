#Задание 1. Код убирающий из списка дубликаты.
# a = [1, 2, 2, 4, 11, 2, 3, 1]
# print(a)
# set1 = set(a)
# print(set1)

# Задание 2. Удаление 0, 4 и 5 элементов списка.
# a = ['John', 'Anna', 'Raychel', 'Katarina', 'Marko', 'Tom']
# print(a)
# element1 = a.pop(0)
# element2 = a.pop(3)
# element3 = a.pop(3)
# print(element1)
# print(element2)
# print(element3)

# Задание 3. сортировка списка в обратном порядке.
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list1)
# list1.reverse()
# print(list1)

# Задание 4. Замена элемента списка на новый.
# list1 = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'october', 'sunday']
# print(list1)
# list2 = list1.copy()
# list2.remove('october')
# list2.insert(5, 'saturday')
# print(list2)

# Задание 5. Ввод слов через пробел, сортировка внесенных данных по кол-ву символов.
# list1 = input('Введите несколько слов через пробел: ')
# a = list1.split()
# a.sort(key=len)
# print(a)
# print(type(a))

# Задание 6. Код для проверки существует ли ключ в dict.
# dict1 = {1: 2, 3: 5, 6: 3, 7: 1}
# print(dict1.keys())
# key_ = dict1.get(1)
# print(key_)

# Задание 7. Программа для объединения двух словарей в один.
# dict1 = {'book1': 'white fang', 'book2': 'witches loaves', 'book3': 'uncle Toms cabin'}
# print(dict1)
# dict2 = {'book4': 'face to face', 'book5': 'all of the stars'}
# dict1.update(dict2)
# print(dict1)

# Задание 8. Программа для сортировки dict по ключам.
# dict1 = {1: 2, 3: 5, 6: 3, 7: 1, 2: 9, 4: 4}
# dict2 = list(dict1.keys())
# dict2.sort()
# print(dict2)

# Задание 9. Код, который проверяет пуст ли словарь.
# dict1 = {1: 2, 3: 5, 6: 3, 7: 1, 2: 9, 4: 4}
# print(dict1.keys())
# print(dict1.values())

# Задание 10. Создать список, внести три новых элемента, сделать список неизменяемым.
# nums = [1, 2, 3]
# nums2 = [4]
# nums3 = {5, 6}
# nums4 = [7]
# nums.extend(nums2)
# nums.extend(nums3)
# nums.extend(nums4)
# print(nums)
# nums = tuple(nums)
# print(nums)

# Задание 11. Программа спрашивает логин и пароль. Записать данные в dictionary и вывести результат.
# login = input('Введите Ваш логин ')
# password = input('Введите Ваш пароль ')
# dict1 = {login: password}
# print(dict1)

# Задание 12. Проверка букв являются ли они гласными или согласными.
# letter = input('Введите любую букву алфавита: ')
# l = letter.upper()
# if l == 'А' or l == 'Е' or l =='Ё' or l == 'И' or l == 'О' or l == 'У' or l == 'Ы':
#     print(f'{l} - гласная буква')
# elif l == 'Э' or l == 'Ю' or l == 'Я':
#     print(f'{l} - гласная буква')
# else:
#     print(f'{l} - согласная буква')

# Задание 13. Есть корзина наполненная n количеством яблок. Так же есть x количество студентов.
# Разделите яблоки поровну между всеми студентами. Если студентов больше чем яблок, то оставьте их в корзине.
# Выведите в результат количество студентов, количество яблок и остаток в корзине.
# n = int(input('Введите количество яблок в корзине: '))
# x = int(input('Введите количество студентов: '))
# if n > x:
#     def func1():
#         print(f'Каждый студент получил по {n // x} яблок' + ' ' + f'остаток в корзине {n % x}')
#     func1()
# if x > n:
#     ost = n - n // x
#     print(f'Студентов {x}, яблок в корзине {n}, остаток яблок в корзине {ost}')

# Задание 14. Для обустройства учебного кабинета необходимо приобрести парты. Количество учеников вводит пользователь.
# Необходимо определить сколько парт нужно купить, если ученики сидят по двое за одной партой.
# Так же если учеников нечетное количество, то кто-то будет сидеть один за партой.
# students = int(input('Введите количество учеников: '))
# def func1():
#     tables = students // 2
#     tables2 = students % 2
#     if tables2 == 0:
#         print(f'Необходимое кол-во парт {tables}')
#     elif tables2 != 0:
#         print(tables + tables2)
# func1()

# Задание 15. Напишите программу для расчета возраста собаки в человеческих годах. Пользователь может ввести возраст и
# размер (маленькая, средняя, крупная). Для вычисления умножте возраст собаки на 9 человеческих лет за каждый собачий
# для маленьких собак; 10,5 лет для средних собак; 12,5 лет для крупных собак.
# age = int(input('Укажите возраст собаки: '))
# size = input('Укажите размер собаки (маленькая, средняя, крупная): ')
# def func1():
#     if size.lower() == 'маленькая':
#         print(age * 9)
#     elif size.lower() == 'средняя':
#         print(age * 10.5)
#     elif size.lower() == 'крупная':
#         print(age * 12.5)
# func1()

# Задание 16. Пользователь вводит три числа. Если все числа больше 10, то вывести на экран yes, иначе no.
# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))
# num3 = int(input('Введите третье число: '))
# def func1():
#     if num1 >= 10 and num2 >= 10 and num3 >= 10:
#         print('yes')
#     elif num1 < 10 and num2 < 10 and num3 < 10:
#         print('no')
# func1()

# Задание 17. Дано три числа. Найти количество положительных чисел среди них.
# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))
# num3 = int(input('Введите третье число: '))
# list_ = [num1, num2, num3]
# print(list_)
# counter = 0
# for i in list_:
#     if i > 0:
#         counter = counter + 1
# print(f'Положительных чисел {counter}')

# Задание 18. Составить в интерпретаторе Python программу которая:
# - просит пользователя ввести целое число и присваивает его переменной num
# - просит пользователя ввести множитель для возведения в степень и присваивает его переменной step
# - проверяет истинность условия, что введенное пользователем целое число num меньше 100
# - если это условие ИСТИННО, то необходимо возвести число num в степень step и присвоить результат переменной result.
# Результат вывести на печать
# - если результат проверки ЛОЖЬ, то вывести на печать сообщение: "Введенное вами число > 100".
# num = int(input('Введите целое число: '))
# step = int(input('Введите множитель для возведения в степень: '))
# if num <= 100:
#         print(num ** step)
# elif num > 100:
#     print('Введенное Вами число > 100')

# Задание 19. Вводятся три целых числа. Определить какое из них наибольшее.
# Пусть a, b, c - переменные, которым присваиваются введенные числа, а переменная m в конечном итоге должна будет
# содержать значение наибольшей переменной.
# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# c = int(input('Введите третье число: '))
# m = a
# if m < b:
#     m = b
# if m < c:
#     m = c
# print(m)

# Задание 20. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))
# num3 = int(input('Введите третье число: '))
# if num1 > num2 and num1 < num3:
#     print(input('Первое число среднее'))
# elif num2 > num1 and num2 < num3:
#     print('Второе число среднее')
# elif num3 > num1 and num3 < num2:
#     print('Третье число среднее')