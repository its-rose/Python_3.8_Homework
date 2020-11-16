# Задание 1.

# class Animal():
#
#     def __init__(self, name, hunger):
#         self.name = name
#         self.hunger = hunger
#     def eat(self):
#         self.hunger += 1
#         print('animal is eating')
#
#     def status(self):
#         print(f'hunger of {self.name}: {self.hunger}')
#
# class Cat(Animal):
#     def meow(self):
#         if self.hunger > 5:
#             self.hunger -= 1
#             print('Meow!')
#         else:
#             print(f'hunger {self.name} = {self.hunger}')
#
# class Dog(Animal):
#     def bark(self):
#         if self.hunger > 5:
#             self.hunger -= 1
#             print('Woof!')
#         else:
#             print(f'hunger {self.name} = {self.hunger}')
#
# cat = Cat('Lily', 3)
# cat.meow()
# cat.status()
# cat.eat()
# cat.eat()
# cat.eat()
# cat.status()
# cat.meow()
#
# dog = Dog('Sharik', 5)
# dog.bark()
# dog.status()
# dog.eat()
# dog.status()
# dog.bark()


# Задание 2.

# class Car():
#     def __init__(self, make, model, year, odometer=0, fuel=70):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer = odometer
#         self.fuel = fuel
#
#     def drive(self, distance):
#         self.distance = distance
#
#         if distance/10 <= self.fuel:
#             def _add_distance(self):
#                 self.odometr += self.distance
#
#             def _subtract_fuel(self):
#                 self.fuel -= distance/10
#
#             print('Lets Drive!')
#         else:
#             print('Need more fuel, please, fill more!')
#
# car1 = Car('Honda', 'Accord', '2003', 0, 40)
# car1.drive(25)

# Задание 3.

# class List():
#     name = 'default'
#     contact = 'default'
#     address = 'default'
#
#     def set_(self, name, contact, address):
#         self.name = name
#         self.contact = contact
#         self.address = address
#
# Kirill = List()
#
# Kirill.set_('Kirill', '0555000000', 'Bishkek')
# k = Kirill = (Kirill.name, Kirill.contact, Kirill.address)
#
# Roza = List()
# Roza.set_('Roza', '0558707111', 'Bishkek')
# r = Roza = (Roza.name, Roza.contact, Roza.address)
#
# class ContactList(List):
#     name = 'Roza'
#
#     def search_by_name(self, name):
#         self.name = 1
#
# all_contacts = [Kirill, Roza]
# all_contacts = ContactList()
# all_contacts.search_by_name(1)

# for i in range(0, 2):
#     all_contacts.name = input('Input name: ')
#
#     if all_contacts.name == 'Kirill':
#         print(k)
#     elif all_contacts.name == 'Roza':
#         print(r)

# Или

# for i in range(0, 2):
#     all_contacts.name = input('Input name: ')
#     if all_contacts.name in k:
#         print(k)
#     elif all_contacts.name in r:
#         print(r)


# Заданеи 4.

# class House():
#
#     def __init__(self, S):
#         self.S = S
#
# class Furniture(House):
#
#     def fur(self, locker, table, bed):
#         self.locker = locker
#         self.table = table
#         self.bed = bed
#
# s = int(input('Укажите площадь дома: '))
# locker = int(input('Площадь шкафа:'))
# table = int(input('Площадь стола: '))
# bed = int(input('Площадь кровати: '))
# a = Furniture(s)
#
# a.fur(locker, table, bed)
# print(f'Площадь дома: {a.S},\n список мебели в доме: шкаф, стол, кровать.')
#
# fur = (a.S - (a.locker + a.table + a.bed))
#
# if fur > 0:
#     print(f'Оставшаяся свободная площадь дома {fur} кв.м.')
# else:
#     print('Места для мебели нет.')
