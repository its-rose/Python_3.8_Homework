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
# key_ = dict1.get(9)
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

#