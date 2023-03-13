# # Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

# # *Пример:*

# # 2 2
# #     4 

def summ(numA, numB):
    if numA == 0:
        return numB

    return summ(numA - 1, numB + 1)


a = int(input('Введите число A: '))
b = int(input('Введите число B: '))

print(f'{a} + {b} = {summ (a, b)}')