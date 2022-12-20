#                                                                Данные, функции и модули в python
# 
#                                   ФАЙЛЫЙ
# a- открытие для добавление данных
# r-открытие для чтения данных
# w-открытие для записи даннх\\ перезаписывание файла сначала
# w+, r+

# colors=['red','green','blue312']
# data=open('file.txt', 'a') # a r w -то что хотим сделать с файлом
# data.writelines(colors)# разделителей не будет
# data.write('\nLINE 2\n')
# data.write('\nLINE 3\n') #\n разделитель между строк- можно ставить в начала или в конце
# data.close()- закрывает работу с файлом(разрывает соединение)

#                           ИЛИ ЛУЧШЕ ИСПОЛЬЗОВАТЬ (аналог выше написанного кода в другом формате)
# with open ('file.txt','a') as data:# as datat -закрывает работу с файлом
#     data.write('line 111111\n')
#     data.write('line 222211\n')

#                           Чтение файла
# path = 'file.txt' # задаем путь к файлу
# data=open(path, 'r') # открывет файл в режиме чтения
# for line in data : # с помощью цикла line пробегаемся по файлу
#     print(line) #считываем все строки
# data.close() # разрыв связи с файлом
# exit()

#                                   ФУНКЦИИ И МОДУЛИ
# Пример описания функции:
# def function_name(x):
#     body line 1
#     ....
#     body line n
#     optional return
# Каким образом разбить приложение что бы в нем не было 1000 строк кода.
# В данному случае мы можем оперделить некоторое количество скриптов, файлов,
# в которых будем складывать одельный функционал программы.

# import lection1 as l# as l-называется АЛИАС- можно задать 1ну буку из нужного файла что бы потом использовать эту букву вместо всего слова

# print(l.f(1))# выводим из lection1 if x==1:-> return 'Целое'


#                                   ФУНКЦИИ
# def new_string(symbol, count=3):
#     return symbol * count

# print(new_string('!',5))#!!!!!
# print(new_string('!'))#!!!
# print(new_string(4))#12-число в скобках(4)будет умнежено на count(=3)
# print(new_string('!'))#TypeError missing 1 required ...

#Возможность передачи неограниченного количества аргументов
# def concatenation (*params):# *число-указываем количество аргументов для передачи
#     res: str =""# ДЛЯ СТРОК
#     for item in params:
#         res +=item
#     return res
# print(concatenation('a','s','d','w'))#asdw
# print(concatenation('a','1','d','2'))#a1d2
# # print(concatenation('1','2','3','4'))#TypeError missing 1 required ...

# def concatenation (*params):# *число-указываем количество аргументов для передачи
#     res: int =0 # ДЛЯ ЦИФР
#     for item in params:
#         res +=item
#     return res
# print(concatenation(1,2,3,4))# 10


#                                   РЕКУРСИЯ(функция вызывающая сама себя)

# Главное в рекурсии указать в какой момент нужно перестать ее вызывать

# def fib(n): #указали название, указали аргумент
#     if n in [1,2]:# прописали логику выхода
#         return 1# возвращаем единицу
#     else: # иначе мы 
#         return fib(n-1)+ fib(n-2)# возвращаем рекурсивный вызов для n-1 и n-2

# list =[]
# for e in range (1,13):# рекурсия проделывается для первых 10 чисел(диапозон задается самостоятелньо)
#     list.append(fib(e))
# print(list)# 1 1 2 3 5 8 13 21 34


#                                   КОРТЕЖИ

#Кортеж- это неизменяемы "список"
# t=()
# print(type())   # tuple
# t=(1,)
# print(tupe(t))  # tuple
# t=(1)
# print(tupe(t))  # int
# t=(28,9,1990)
# print(tupe(t))  # tuple
# colors=['red','green','blue']
# print(tupe(t))  # ['red','green','blue']
# t=tuple(colors)
# print(t)        # ('red','green','blue')

#ДЛЯ INT
# a=(3,4,45,4) #a=3,b=4
# print(a)
# print(a[0]) #3-обращение к элементу с индексом 0 в кортеже
# print(a[-2])#45

# t=tuple(['red','green','blue'])
# print(t[0])     # red
# print(t[2])     # green
# # print(t[10])    # IndexError: tuple index out of range
# print(t[-2])    # green

# for e in t:   # перебор кортежа с помощью цикла
#     print(e, end=' ')      # red green blue

# t[0]= 'black'     # TypeError: 'tuple' object does not support item assignment


#                                 СЛОВАРИ

# #Словари- неупорядоченные коллекции произвольных объектов с доступом по ключу
# dictionary={}
# dictionary=\
#     {
#         'up': '↑',  # ключ- значение слева(up), значение то что справо(↑)
#         'left': '←',
#         'down': '↓',
#         'right': '→'
#     } 
# #dictionary=\-обратный слеш ставится что бы не писать все в одну строку 
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}     посмотреть весь словарь-print
# print(dictionary['left']) # ←       посмотреть определенное значение при обращении к ключу
# # типы ключей могут отличаться

# print(dictionary['up']) # ↑

# dictionary['left']='⇐'  # присовение нового значения ключу
# print (dictionary['left'])  # ⇐
# del dictionary(['left'])    # удаление элемента

# for item in dictionary:
#     print('{}: {}'. format(item, dictionary[item]))
# # up: ↑
# # down: ↓
# # right: →


#                                   МНОЖЕСТВА
# Неупорядоченная совокупность элементов
# a = {1, 2, 3, 5, 8}
# b = {'2', '5', 8, 13, 21}
# print(type(a)) # set
# print(type(b)) # set

# a = {1, 2, 3, 5, 8}
# b = set([2, 5, 8, 13, 21])
# c = set((2, 5, 8, 13, 21))
# print(type(a)) # set
# print(type(b)) # set
# print(type(c)) # set
# a = {1, 1, 1, 1, 1}
# print(a) # {1}

# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }
# # print(colors) # set()


# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()            # c={1, 2, 3, 5, 8}
# u= a. union(b)          #u = {1, 2, 3, 5, 8, 13, 21}
# i= a.intersection(b)    # пересечение i= {8, 2, 5}
# dl = a.difference(b)    #dl = {1, 3}
# dr = b.difference(a)    #dr = {13, 21}

# q = a \
#  .union(b) \
#  .difference(a.intersection(b))
# # {1, 21, 3, 13}

# #Замороженное множество
# s=frozenset(a)
# # тут никакие методы изменения работать не будут

#                                       СПИСКИ
# list1=[1,2,3,4,5]
# list2=list1

# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)

# list1[0]=123
# list2[1]=333
# print()

# for e in list1:
#     print(e)

# print()

# for e in list2:
#     print(e)



# list1=[1,2,3,4,5]

# print(len(list1))
# print(list1.pop())      #метод pop извлекает последний элемент в списке
# print(list1)
# print(list1.pop())
# print(list1)

# если нужно удалить конкретный элемент в списке
# list1=[1,2,3,4,5]
# print(list1)
# print(list1.pop(2))
# print(list1)

# если нужно добавить элемент в список
# list1=[1,2,3,4,5]
# print(list1)
# print(list1.insert(2,11))   # функция insert- добавление в индекс 2 значения 11
# print(list1)
# print(list1.append(123))    # функция append- добавляет значение в конец списка
# print(list1)