# Задание 1. Создайте класс Shop, имеющий следующие параметры: name, is_open,
# products_list и методы, имитирующие работу магазина (add_products, is_available, buy_product).
# Если в products_list содержатся продукты, то is_open должен быть равен True. Если не содержатся, то False.
# Создайте 1 объект класса и попробуйте все его методы.

# class Shop():
#     def __init__(self, name, is_open, products_list):
#         self.name = name
#         self.products_list = ['апельсины', 'яблоки', ',бананы']
#         if len(self.products_list) > 0:
#             self.is_open = True
#         else:
#             self.is_open = False
#
#
#     def add_products(self):
#         a = input('Введите товар, который необходимо добавить в магазин: ')
#         self.products_list.append(a)
#
#     def is_available(self):
#         print(f'В магазине имеются следующие товары: {self.products_list}')
#
#     def buy_product(self):
#         input('Укажите наименование продукта, который Вы хотите купить: ')
#         print('Спасибо за покупку!')
#
# my_shop = Shop('Фруктовый', True, '')
# my_shop.add_products()
# my_shop.is_available()
# my_shop.buy_product()


# Задание 2. Напишите класс Employee, конструктор которого имеет параметры: имя, фамилия, должность, зарплата.
# Добавьте метод get_info(), который выводит информацию о сотруднике в отформатированном виде:
# «*name* *last_name*, работает на должности *position* и получает зарплату в размере *salary* сом.»

# class Employee():
#     def __init__(self, name, last_name, position, salary):
#         self.name = name
#         self.last_name = last_name
#         self.position = position
#         self.salary = salary
#
#     def get_info(self):
#         print(f'{self.name} {self.last_name} '
#               f'работает на должности {self.position} '
#               f'и получает зарплату {self.salary}, сом.')
#
# employee1 = Employee('John', 'Murphy', 'python junior developer', 100000)
# employee1.get_info()


# Задание 3. Создайте класс Child с параметрами name, apples. Создайте несколько экземпляров класса.
# Выведите в результат общую сумму яблок всех детей.

# num_of_apples = []
# class Child():
#     def __init__(self, name, apples):
#         self.name = name
#         self.apples = apples
#         num_of_apples.append(self.apples)
#         a = sum(num_of_apples)
#         print(f'Общее количество яблок у детей: {a}')
#
# child1 = Child('Roza', 2)
# child2 = Child('Atay', 5)
# child3 = Child('Nursultan', 10)
# child4 = Child('Ajara', 15)


# Задание 4. Напишите класс Person, который принимает в качестве параметров имя, фамилию и год рождения.
# Напишите функцию get_age, которая выводит в результат: «*name* *last_name*, тебе *age* лет.»

# class Person():
#     def __init__(self, name, last_name, date_of_birth):
#         self.name = name
#         self.last_name = last_name
#         self.date_of_birth = date_of_birth
#
#     def get_age(self):
#         age = 2020 - self.date_of_birth
#         print(f'{self.name} {self.last_name}, тебе {age} лет.')
#
# me = Person('Roza', 'Seitakhunova', 1994)
# me.get_age()


# Задание 5. Implement Students room using OOP:
# Steve = Student("Steven Schultz", 23, "English")
# Johnny = Student("Jonathan Rosenberg", 24, "Biology")
# Penny = Student("Penelope Meramveliotakis", 21, "Physics")
# print(Steve)
# <name: Steven Schultz, age: 23, major: English>
# print(Johnny)
# <name: Jonathan Rosenberg, age: 24, major: Biology>

# class Students():
#     def __init__(self, name, last_name, age, major):
#         self.name = name
#         self.last_name = last_name
#         self.age = age
#         self.major = major
#
#     def output(self):
#         print(f'{self.name} {self.last_name}, age {self.age}, major: {self.major}')
#
# Steve = Students('Steven', 'Schultz', 23, 'English')
# Johnny = Students('Jonathan', 'Rosenberg', 24, 'Biology')
# Penny = Students('Penelope', 'Meramveliotakis', 21, 'Physics')
# Steve.output()
# Johnny.output()
# Penny.output()