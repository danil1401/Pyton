                                                        # Урок 6.
                                                        # Повторение списков


# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод:
# 7
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1
# Вывод:
# 3 3 2 12
# (каждое число вводится с новой строки)

# N = int(input('Введите число элементов первого массива: '))
# massiv_1 = [int(input('Введиет сам элемент массива: ')) for i in range(N)]
# M = int(input('Введите число элементов второго массива: '))
# massiv_2 = [int(input('Введиет сам элемент массива:')) for i in range(M)]

# print(*massiv_1)# звездочка * убирает квадратные скобки массива
# print(*massiv_2)

# for i in massiv_1:
#     if i not in massiv_2:
#         print(i, end=' ')# end= ' ' указывается что бы числа выводились в одну строку, разделяясь пробелом(в кавычках можно указать что угодно)



# Задача №41. 
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.

# from random import randint
# n=int(input('Введите количество элементов списка: '))
# lst=[randint(1,n) for _ in range(n)]
# print(f'Первоначальный массив : {lst}')

# count=0
# for i in range(1,len(lst)-1):
#     if lst[i-1]<lst[i]>lst[i+1]:
#         count+=1
# print(count)


# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод:
# 1 2 3 2 3 
# Вывод: 2

# from random import randint
# n=int(input('Введите количество элементов списка: '))
# lst=[randint(1,n) for _ in range(n)]
# # lst=(1,2,3,2,3)
# print(lst)
# count=0

# for i in range(len(lst)):
#     for j in range(i+1,len(lst)):
#         if lst[i]==lst[j]:
#             count+=1
# print(count)



# Задача №45. Решение в группах
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод: 
# 300 
# Вывод:
# 220 284