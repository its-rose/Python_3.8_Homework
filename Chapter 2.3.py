# Задание 1. Введите строку через терминал. Обработайте ошибку, при которой значения в строке не являются числовыми.
# (Код должен принимать только числовые значения).
# string_ = input('Введите любой текст: ')
# list_ = []
# list_.append(string_)
# try:
#         list(map(int, list_))
# except ValueError:
#     print('!!! В строке не все элементы числа.')
# else:
#     print('Строка проверена. Все элементы - числа.')

# Задание 2. Создайте список. Напишите обработку ошибки, при которой введен несуществующий индекс списка.
# list1 = [i for i in range(0, 6)]
# try:
#     print(list1[7])
# except IndexError:
#     print('Указан индекс несуществующего элемента.')

# Задание 3. Обработайте ошибку KeyError, используя dictionary.
# dict_ = {'book1': 'white fang', 'book2': 'witches loaves', 'book3': 'uncle Toms cabin', 'book4': 'face to face',
# 'book5': 'all of the stars'}
# try:
#     print(dict_['movie'])
# except KeyError:
#     print('Такого ключа нет в словаре.')

# Задание 4. Обработайте любой код, применив 2 любых исключения. Для каждого из них напишите разные результаты в выводе.
# print('Для расчета остатка от деления двух чисел, введите исходные данные.')
# num1 = input('Введите первое число (делимое): ')
# num2 = input('Введите второе число (делитель): ')
# try:
#     num1 = int(num1)
#     num2 = int(num2)
#     print(num1 % num2)
# except ValueError:
#     print('Внимание! В одной из переменной введено не число.')
# except ZeroDivisionError:
#     print('Делитель не должен быть равен 0.')

# Задание 5. Обработайте ошибку IndexError. Напишите разные результаты при нахождении и отсутствии ошибки.
# monthes = ['January', 'February', 'March', 'April', 'May']
# try:
#     print(monthes[2])
#     element = monthes[2]
# except IndexError:
#     print('Указан индекс несуществующего элемента.')
# else:
#     print(f'Под указанным Вами индексом сохранен элемент {element}')

# Задание 6. К предыдущему коду добавьте сообщение "Проверка завершена", при любом исходе обработки.
# monthes = ['January', 'February', 'March', 'April', 'May']
# try:
#     print(monthes[2])
#     element = monthes[2]
# except IndexError:
#     print('Указан индекс несуществующего элемента.')
# else:
#     print(f'Под указанным Вами индексом сохранен элемент {element}')
# finally:
#     print('Проверка завершена')