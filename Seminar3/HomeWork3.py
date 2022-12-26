# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# from random import randint
# list_num= [randint(0,100)for i in  range(randint(5,10))]
# print(list_num)
# sum_num=0

# for i in range(1,len(list_num),2):
#     sum_num+=list_num[i]
# print(sum_num)




# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# from random import randint
# list_num= [randint(0,100)for i in  range(randint(1,9))]
# print(list_num)
# multi=[]

# middle= len(list_num)//2+len(list_num)%2
# for i in range (middle):
#     multi.append(list_num[i]*list_num[-i-1])
# print(multi)





# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# import random

# def drob(num):
#     return round(num%1,2)

# a=[round(random.uniform(0,10),2) for i in range(random.randint(5,8))] # random.uniform-выдает рандомное число во float
# print(a)
# list_drob=list(map(drob,a))
# print(list_drob)

# print(max(list_drob)-min(list_drob))
# print(max(list_drob),min(list_drob))





# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# def dec_to_bin(num, result = ""):
#     if num==0:
#         return result
#     result=str(num%2)+result
#     return dec_to_bin(num//2,result)

# print(dec_to_bin(int(input('Введите значение: '))))




# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# def positive_fib(num):
#     positive_list=[1,1]
#     for i in range (num-2):
#         positive_list.append(positive_list[-2]+positive_list[-1])
#     return positive_list

# def negative_fib(num):
#     negative_list=[0,1]
#     for i in range (num-1):
#         negative_list.append(negative_list[-2]-negative_list[-1])
#     return negative_list [::-1]

# print(negative_fib(8)+ positive_fib(8) )