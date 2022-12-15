# a=3
# b=2
# print('Изначально', a, b)
# a,b=b,a
# print('Смена', a,b)

#                                                   ЗАДАЧА 1
#Написать программу. которая на ход принимает 2 числа и проверяет, явяляется ли одно число квадратом другого
#5,25> да
#8,9> нет

# print ('Ведиет первое число: ')
# first_arg=int(input())
# print(first_arg)
# print ('Ведиет второе число: ')
# second_arg=int(input())
# print(second_arg)

# if (first_arg**2==second_arg):
#     print('Число является квадратом другого')
# elif (second_arg**2==first_arg):
#     print('Число является квадратом другого')
# else:
#     print('Число не является квадратом другого')
# ## elif firstarg**2!=secondarg or secondarg**2!=firstarg:
# #     print('Число не является квадратом другого')

#                                               ИЛИ(упрощенное)!!!

# print ('Ведиет первое число: ')
# first_arg=int(input())
# print ('Ведиет второе число: ')
# second_arg=int(input())
# print(f'Числа: {first_arg},{second_arg}')

# if first_arg**2==second_arg or second_arg**2==first_arg:
#     print('Число является квадратом другого')
# else:
#     print('Число не является квадратом другого')



#                                                    ЗАДАЧА 2
#Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# 1,2,3,4,5>5

# numbers=[]
# for i in range(5):  # range- обозначает длину массива, 
#         # у range есть (start, stop, step)
#         # range(5)-> range(start=0,stop=5,step=1)
#         # range(1,5)->range(start=1,stop=5,step=1)
#         # range(1,5,2)->range(start=1,stop=5,step=2)
#         numbers.append(int(input(f'Введите элемент под номером {i}: ')))    # apped- означает добавить в конец списка следующее вводимое значение
# print(numbers)
# print(f'Длина списка: ', i+1)
# print(f'Максимальное значение: ', (max(numbers)))# max - это функция которая автоматически опред максимальное значение

#                                           ИЛИ ПРОЩЕ
# my_max=0
# for _ in range(5):    #_-таже переменна что и i к примеру
#     num=int(input('Введите число'))
#     if my_max < num:
#         my_max=num
# print(my_max)



#                                                      ЗАДАЧА 3
# Напишите программу, которая принимает на вход число N и выводит числа от -N до N
#-3-2-1 0 1 2 3

# numbers=int(input('введите число: '))
# if numbers<0:
#     numbers*=-1
# for i in range(-numbers, numbers+1):
#     print(i, end=' ')


#                                                       ЗАДАЧА 4
#Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
#6.78->7

# numbers=float(input('Write your numbers: '))
# numbers//=1
# print(numbers)

num=float(input('Write number: '))
if num%1==0:
    print('No')
else:
    num= int(num*10%10)
    print(num)