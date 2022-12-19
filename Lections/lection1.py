#print ("hello w1orld")

#a=123
#b=1.23
#print(type(a))
#print(type(b))
# s='Оператор сторки'# тип данныз str пишется в ''
# # s='Оператор \n сторки'# \n переход на новую строку
# print (s) #
# print(type(s))
# комментарий делается через # в самом начале строки для закомента с самого начала

#print(a,'-',b,'-',s) #пример вывода нескольких переменных
#print('{}-{}-{}'.format(a,b,s))
#print(f'{a}-{b}-{s}')#f вначале для того что бы выввелось значение указанной переменной

#f=True
#f=False
#print(f)

#list=[1,2,3]#объявление массива
#list=['1', '2', '3','Привет мир', 1, 2, 3, 4.5,True]# вывод массива из строк, целочисленных значений, вещественных, логических
#print(list)
#list=['1', '2', '3']
#col= ['Привет мир', 1, 2, 3, 4.5,True]
#print(list)
#print(col)

#                                                                           ВВОД И ВЫВОД ДАННЫХ
#print()- отвечает за вывод данных
#input()-отвечает за ввод данных

# print('Введите a')
# #a=int(input())
# a=float(input())
# # print('Введите b')
# # b=int(input())
# # b=float(input())
# print(a)

#НЕСКОЛЬКО СПОСОБОВ ВЫВЕСТИ ИНФОРМАЦИЮ
# a=2
# b=3
# print(a,b)
# print('{} {}'.format(a,b))#a и b имеют индексы, можно менять индексы в скобках {0} {1} или{1} {0} и будет выводиться по разному присвоенное значение
# print(f'{a} {b}')
# #Вывод какого либо действия между значениями- нужно указать тип переменной в input(т.к по умолчанию у нас строки в input)
# print(a,'+',b,'=',a+b)
#                                                                       АРИФМЕТИЧЕСКИЕ ОПРИЕРАЦИИ
# у PAYTON нет ограничений по количеству памяти как в C#
#+,-,*,%,//,**
#Приоритет операций **,*,/,//,%,+,-
#() Скобки меняют приоритет

#a=123
#a=2 # Унарный плюс
#b=321
#b= 8 #У нарный минус
#c=a/b# По умолчанию деление работает как для вещественных чисел (float)
#c=a//b # Деление будет целочисленных (int)
#c=a%b# Остаток (%)
#c=a**b# возведение в степерь (**)

# a=1.31434
# b=3
# c=round(a*b,3)# round округление числа, если требуется знаки поле запятой, после последней переменной пишем (,3)
# print(c)

# a=2
# # a=a+5# что бы так не писать см. строку ниже
# a*=5# это работает и для других арефметических операций
# print(a)

#                                                                       ЛОГИЧЕСКИЕ ОПЕРАЦИИ
#>,>=,<,<=,==,!=
#not, and, or-не путать с &,|,^
#Еще is, is not, in, not in
#gen

#a=1<3
# a=1<4 and 5>2
# a=1==2
# a=1!=2
# print(a)

# a='21'
# b='21'
# # a=[1,2]
# # b=[1,2]
# print(a==b)

#a=1<3<5<10
#print(a)

# func=1
# T=4
# x=123
# print(func<T>x)

# f=1<2 or 4>6
# print(f)

# f=[1,2,3,4]
# print(f)
# # print(2 in f)# 2 in f показывает есть ли указанная переменна(2) в списке f-ответ будет True
# # print(not 2 in f)# 2 не в списке- ответ False
# # # Факта четности числа
# # is_odd=f[2]%2==0#обращаемся к первому элементу списка под индексом 0(f[0]) и находим остаток от деление % на 2 равый нулю(==0)
# is_odd=f[0]%2
# print(is_odd)

#                                                                   УПРАВЛЯЮЩИЕ КОНСТРУКЦИИ: if, if-else
#if condition: условие
    #operator1 блок операторов
    #...
    #operator n
#else
    #operator n+1
    #...
    #operator n+m

#usermame=input('Введите имя: ')
#if(usermame=='Вика'):
#    print('Ура, это Моя Любимая Вика')
#else:
#    print('Привет', usermame)

#a=int(input('Введите число: '))
#b=int(input('Введите число: '))
#if a>b:
#    print('Макс: ',a)
#else:
#    print('Макс: ',b)

#if condition1:
    #operator
#elif condition2:
    #operator
#elif condition3:
    #operator
#else:
    #operator
#usermame=input('Введите имя: ')
#if(usermame=='Вика'):
#    print('Ура, это Моя Любимая Вика')
#elif usermame=='Марина':
#    print('Добрый день')
#else:
#    print('Привет', usermame)

#                                                           УПРАВЛЯЮЩАЯ КОНСТРУКЦИЯ WHILE

#while condition: условие
    #operator1 блок операторов
    #...
    #operator n
#original=23
#inverted=0
#while original !=0:
#    inverted=inverted*10+(original%10)
#    original//=10
#print(inverted)

#while condition: условие
    #operator1 блок операторов
    #...
    #operator n
#else
    #operator n+1
    #...
    #operator n+m
#original=23
#inverted=0
#while original !=0:
#    inverted=inverted*10+(original%10)
#    original//=10
#    print(original)
#else:
#    print('Пожалуй')
#    print('хватит')
#print(inverted)

#                                                                   УПРАВЛЯЮЩАЯ КОНСТРУКЦИЯ FOR
#for i(счетчик) in enumeration(итерируемый объект):
    #operator1 блок операторов
    #...
    #operator n
#for i in 1,2,3,4,5:
#    print(i**2)

# r=range(10)
# # for i in range(1,5):
# for i in range(1,10, 2): # +2 каждому числу, будут выводиться не четные
# # for i in 'Строка в разбивке':
#    print(i)

#                                                                                    НЕМНОГО О СТОКАХ
#text=' съешь еще этих мягких французких булочек'
#print(len(text))    #39     вывод количества символов в строке
#print('еще'in text) #True   проверка есть ли какое то значение в строке
#print(text.isdigit())   #False  проверка явялется ли все символы в строке числами
#print(text.islower())   #True   проверка являются ли все символы в строке нижнего регистра
#print(text.replace('еще','ЕЩЕ'))    # замена одного значения другим

#for c in text: разбивка по каждому символу
#    print(c)

#help(int)  # вызов помощи в скобках может быть любая фнкция, метод и т.д
#text=' съешь еще этих мягких французких булок'
#print(text[0])  # c-выводи значние под указанным уиндексом в []
#print(text[1])  # ъ-выводи значние под указанным уиндексом в []
#print(text[len(text)-1])    #к-выводи значние с конца от длины массива
#print(text[-5]) #б-выводит с конца указанное значени после вычета указанного количества символов
#print(text[:])  #print(text)
#print(text[:2]) #съ-выводит колическо указанных индексов от 0го до заданного(2)
#print(text[len(text)-2:])   #ок-выводит колическо указанных индексов c конца
#print(text[2:9])    #ешь еще- выводит значения в диапозоне индексов
#print(text[6:-18])  #еще этих мягких- выводит значения в диапозоне индексов
#print(text[0:len(text):6])  #сеикал-
#print(text[::6])    #сеикакл-
#text=text[2:9]+text[-5]+text[:2]    #...

#                                                                                   СПИСКА(МАССИВЫ)
#Списки-пронумерованная, изменяемая коллекция объектов
# numbers=[1,2,3,4,5]
# print(numbers)#[1,2,3,4,5]

# numbers=list(range(1,6))
# print(numbers)# [1,2,3,4,5]

# numbers[0]=10
# print(numbers)#[10,2,3,4,5]
# # for i in numbers:
#     i*=2
#     print(i)#[20,4,6,8,10]
#     print(numbers)#[10,2,3,4,5]
# colors=['red', 'green', 'blue']
# print(colors)
# # for e in colors:
# #     print(e)#red, green, blue

# # for e in colors:
# #     print(e*2)# redred, greengreen, blueblue

# colors.append('gray')# добавить в конец
# print(colors==['red', 'green', 'blue', 'gray']) #True
# colors.remove('red')    # или del colors [0]    #удалить элемент
# print(colors)

#                                                                           ФУНКЦИИ
#Функция это фрагмент программы, который используется многократно

# def function_name(x):
    #body line 1
    #....
    #body line n
    #optional return

# def f(x):
#     if x==1:
#         return 'Целое'
#     elif x==2.3:
#         return 23
#     else:
#         return
# arg=2.3
# print(f(arg))
# print(type(f(arg)))