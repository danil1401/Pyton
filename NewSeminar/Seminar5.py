# Задача №31.
# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

# def fib (n):# функция вывода числа фибоначи по его индексу
#     if n in(0,1):
#         return n
#     return fib(n-1) + fib(n-2)

# print(fib(7))

# Задача №33.
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# lst = [int(input('Введите элементы списка: '))for _ in range(5)]
# x = min(lst)
# y = max(lst)
# lst2 = [x if i == y else i for i in lst]
# print(lst2)

# from random import randint

# n=int(input('Введите количество отметок: '))
# marks=[randint(1,5) for _ in range(n)]
# print(marks)
# min_mark=min(marks)
# max_mark=max(marks)

# for i, val in enumerate(marks):
#     if val== max_mark:
#         marks[i]=min_mark
# print(marks)


# Задача №35.
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 

# num=int (input('Введиет число: '))
# def ostatok (num):# функция проверки числа простое ли?
#     for i in range(2,num//2):
#         if num % i==0:
#             return True 
#             #или можно текстом указать return 'Число правильное'
#     return False
# print(ostatok(num))


# Задача №37.
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

# def revers(n,s=''):
#     if n>0:
#         return revers(n-1,input()+s)
#     return s
# print(f'Обратный порядок {revers(5)}')
