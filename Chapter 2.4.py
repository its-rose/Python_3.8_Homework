# Задание 1. Напишите декоратор, для создания бургера.
# def burger(func):
#     def bur(*args, **kwargs):
#         print('верхняя булочка')
#         func(*args, **kwargs)
#         print('нижняя булочка')
#     return bur
#
# def kotleta(func):
#     def kot(*args, **kwargs):
#         print('курочка')
#         func(*args, **kwargs)
#         print('говядина')
#     return kot
# @burger
# @kotleta
# def nachinka(cheese, tomatoes, cucumber, sous):
#     print('\n', cheese, '\n', tomatoes, '\n', cucumber, '\n', sous, '\n')
# nachinka('сыр', 'помидоры', 'огурцы', 'соус')

# Задание 2. Напишите декоратор, который выводит строку "Результат выполнения вашей функции: " и сам результат.
# Используйте 2 любые математические функции.
# def math(func):
#     def count(*args, **kwargs):
#         print('Результат выполнения Вашей функции: ')
#         func(*args, **kwargs)
#     return count
# @math
# def num1(a, b):
#     result1 = a // b
#     print(result1)
# num1(25, 3)
# @math
# def num2(a, b):
#     result2 = a % b
#     print(result2)
# num2(85, 24)

# Задание 3. Напишите декоратор, который создает дом. У дома должно быть основание и крыша. Добавьте этажи или комнаты
# (если дом одноэтажный) с помощью функций.
# def roof_foundation(func):
#     def home(*args, **kwargs):
#         print('крыша')
#         func(*args, **kwargs)
#         print('основание')
#     return home
# def floor2(func):
#     def fl(*args, **kwargs):
#         print('второй этаж:')
#         print('спальня,', 'детская,', 'гостевая комната')
#         print('лестница')
#         func(*args, **kwargs)
#     return fl
# @roof_foundation
# @floor2
# def floor1(*args, **kwargs):
#     print('первый этаж:')
#     print('гостиная,', 'столовая,', 'кухня,', 'ванная комната')
# floor1()
