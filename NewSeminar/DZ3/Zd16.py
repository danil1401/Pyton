# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

n=int(input('Введите количество эдементов в списке: '))
arr=[int(input('Введите число для списка')) for i in range(n)]
print(arr)
x=int(input('Введите нужное число: '))
print(f'Число {x} встречается в списке {arr.count(x)} раз')