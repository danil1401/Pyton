#                                                                 Задача 6
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
#     - 6 -> да
#     - 7 -> да
#     - 1 -> нет

# day_week=int(input('Write your number of week: '))

# print(f'Numbers day of Week: ', day_week)

# if (day_week>=1 and day_week<=5):
#     print('HARD WORK')
#     print(day_week>=6)
# elif(day_week>=6 and day_week<=7):
#     print('HOLLYDAYS!!!')
#     print(day_week>=6)
# else:
#     print('Retur and write from 1 before 7')

#Защита от дурака
# day_week=int(input('Write your number of week: '))
# while day_week not in('1','2','3','4','5','6','7') and day_week !='exit':
#     day_week=int(input('Write your number of week: '))

# if day_week.isdigit():# is digit -является цифрой
#     day_week=int(day_week)#эти строчки можно убрать т.к ранее было присвоение int
#     print ('Номер дня недели', day_week)


#                                                                 Задача 7
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ⋀-and
# ⋁-or
# ¬-not

# x=float(input('Write X: '))
# y=float(input('Write Y: '))
# z=float(input('Write Z: '))
# print((not(x or y or z)) == (not(x) and not(y) and not(z)))

#                                                                 Задача 8
# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# print('Write X: ')
# x=int(input())
# print('Write Y: ')
# y=int(input())
# print(f'Coordinates X and Y: ', x,'and', y)

# if (x >0 and y >0):
#     print('1 quater')
# elif(x>0 and y<0):
#     print('4 quater')
# elif(x<0 and y<0):
#     print('3 quater')
# elif(x<0 and y>0):
#     print('2 quater')
# else:
#     print('Try again')

#                                                                 Задача 9
# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# print('Write number of quater form 1 before 4: ')
# number=int(input())
# print(f'Number of quater: ', number)

# if( number==1):
#     print('X= from 1 before infinite and Y=from 1 before infinity')
# elif(number==2):
#     print('X= from 1 before infinite and Y=from -1 before infinity')
# elif(number==3):
#     print('X= from -1 before infinite and Y=from -1 before infinity')
# elif(number==4):
#     print('X= from -1 before infinite and Y=from 1 before infinity')
# else:
#     print('Try again')

#                                                                 Задача 10
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# while (True):
#     try:
#        a=list(map(float,input('insert A(x1,y1), for example: "3 whitespace 6" : ').split()))
#        break
#     except Exception: print('Error: Check your value!')
# while (True):    
#     try:
#        b=list(map(float,input('insert B(x2,y2), for example: "2 whitespace 1" : ').split()))
#        break
#     except Exception: print('Error: Check your value!')
# print(f'Distanse between A{a} and B{b} is: {round(((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5,3)}')


