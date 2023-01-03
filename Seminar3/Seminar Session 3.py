import os
os.system('clear') # отчистка консоли

#                                               ЗАДАЧА  
# Реализуйте алгорит задания случайных числе без встроенного генератора псевдослучайных числе

# import time
# current_time=time.time()
# print(current_time)
# rand_num=int(1000*current_time)
# print(rand_num)
# print(rand_num % 100)
# print(str(rand_num)[-5:])

#                                               ЗАДАЧА  
# Задайте список. Напишите ПО которая определит, присутсвует ли в заданном списке строк некое число

# list=["2", "43", "5", "331", "91", "35", "79", "53"]

# x=input('Введите число: ')
# for i in list:
#     if x==i:
#         print(f'Число {i} есть в списке')
#         break #завершает чикл когда число найдется без перебора остальных
# else:
#     print('Таких цифр нет. ')

#                                               ЗАДАЧА 

# Напишите программу, которая определит позицию второго вхождения строки в списке, либо сообщит что ее нет.
# my_list=['123', 'ghb','32','enter']
# print(my_list)
# string_find='123'
# count=0
# for i in range(len(my_list)):
#     if string_find == my_list[i]:
#         count+=1
#         if count==2:
#             print(i)
# else:
#     print(-1)
