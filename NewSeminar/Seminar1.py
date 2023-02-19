#                                                       ВВОД - ВЫВОД, ОПРЕАТОРЫ ВЕТВЛЕНИЯ
# Задача №1. 
# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# n=700 // m=750

# n=700
# m=750
# print ('Количество дней что бы проехать маршрут: ',round((m/n),2), 'дня')



# Задача №3.
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

# import math # вызов библиотеке для применения функции math.ceil
# students= int(input('Количество учеников в классе: '))
# print('Необходимое количество парт:', math.ceil(students/2)) # функция math.ceil округляет число в большую степень


# Задача №5.
# Вагоны в электричке пронумерованы натуральными
# числами, начиная с 1 (при этом иногда вагоны
# нумеруются от «головы» поезда, а иногда – с
# «хвоста»; это зависит от того, в какую сторону едет
# электричка). В каждом вагоне написан его номер.
# Витя сел в i-й вагон от головы поезда и обнаружил,
# что его вагон имеет номер j. Он хочет определить,
# сколько всего вагонов в электричке. Напишите
# программу, которая будет это делать или сообщать,
# что без дополнительной информации это сделать
# невозможно.
# Input: 3 4(ввод на разных строках)
# Output: 6

# i=int(input('Номер вагона от головы: '))
# j=int(input('Номер вагона присвоенный: '))

# if i==j:
#     print('Определить не удается')
# else:
#     print('Общее количество вагонов', i+j-1) # (f'Общее количество вагонов {i+j-1}')


# Задача №7.
# Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным. Если
# год является високосным, то выведите YES, иначе
# выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен
# 100, а также если он кратен 400.
# Input: 2016
# Output: YES

year=int(input('Номер года: '))

if year % 4 ==0 and year %100!=0 or year %400==0:
    print('Да')
else:
    print('Нет')
