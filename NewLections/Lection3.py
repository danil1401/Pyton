                                # Урок 3. Функции, рекурсия, алгоритмы

                                    # Функции
# Функция — это фрагмент программы, используемый многократно.
# Мы знакомы уже с функциями с C#, давайте теперь посмотрим, как
# создаются и используются функции внутри Python
# def function_name(x):
#  # body line 1
#  # ...
#  # body line n
#  # optional return


#             Задача
# Необходимо создать функцию sumNumbers(n), которая будет
# считать сумму всех элементов от 1 до n.
# Решение:
# 1. Необходимо создать функцию:
# def sumNumbers(n):
# Очень важно понимать одну вещь, сколько аргументов мы передаем,
# столько и принимаем. Или наоборот сколько аргументов мы
# принимаем, столько и передаем.
# В нашем случае функция sumNumbers принимает 1 аргумент(n).
# принимает 1 аргумент(n).

# def sum_numbers(n):
    # summa=0
    # for i in range(1, n+1):
    #     summa +=i
    # print(summa)

# sum_numbers(2)# таким образом вызывается выше написанная функция, в скобках число которая функция преобразовывает

# def sum_numbers(n, y='Hello'):
#     print(y)
#     summa=0
#     for i in range(1, n+1):
#         summa +=i
#     return summa #return завершает работу
#     print('stop')# проверка завершения работы
# a=sum_numbers(5)
# print (a)

# def sum_str(*args):
#     res=''
#     for i in args:
#         res+= i
#     return res

# print(sum_str('q', 'e', 'r'))
# print(sum_str('q', 'e', 'r', 'l', 'l'))
# print(sum_str(1,8,9))

#                                                                           Модульность(место хранения функций)
# Вы когда-нибудь задавались вопрос, как например работает функция .append
# Это же точно такая же функция, как и sumNumbers(n), но мы ее нигде не создаем,
# все дело в том что, это функция автоматически срабатывает и чтобы ей
# пользоваться ничего дополнительно писать не надо.
# Представьте себе такую ситуацию, что Вы создаете огромный проект и у Вас
# имеется большое количество функций, к примеру 5 функций работают со
# словарями, 18 со списками и тд. и у каждой функции свой алгоритм, но их
# объединяет работа с одной коллекцией данных. Согласитесь неудобно работать в
# таком большом файле, где около 80 функций, очень легко потеряться и на
# перемотку кода Вы будете терять драгоценное время. Решение данной проблемы
# есть. Давайте будем создавать отдельные файлы, где будут находиться только
# функции, и эти функции при необходимости вызывать из главного файла.

# import modul1# импорт модуля из файла modul1.py в дереве
# print(modul1.max1(5,9))# вызываем функцию max1 из модуля который теперь подтянулся выше

#       Либо вызвать функцию по другому из модуля в дереве.
# from modul1 import max1
# print(max1(10,4))

# #       Либо, если мы хотим использовать несколько функций, их можно не перечислять а прописать только *
# from modul1 import *# * звездочка вызывает все функции в модуле
# print(max1(33,141))# max1 название функции в модуле.

#           Можно скоратить название модуля если оно большое
# import modul1 as m1
# print(m1.max1(10,3))# теперь можно указать не modul1 а m1




#                                                                           Рекурсия
# Рекурсия — это функция, вызывающая сама себя.
# Пользователь вводит число n. Необходимо вывести n - первых
# членов последовательности Фибоначчи.
# Напоминание: Последовательно Фибоначчи, это такая последовательность, в
# которой каждое последующее число равно сумму 2-ух предыдущих.
# При описании рекурсии важно указать, когда функции надо остановиться и
# перестать вызывать саму себя. По-другому говоря, необходимо указать базис
# рекурсии

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n - 1) + fib(n - 2)

# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))
# print(list_1) # [1, 1, 2, 3, 5, 8, 13, 21, 34]


#                                                                         Алгоритмы
# Алгоритмом называется набор инструкций для выполнения
# некоторой задачи. В принципе, любой фрагмент
# программного кода можно назвать алгоритмом, но мы с
# Вами рассмотрим 2 самых интересных алгоритмы
# сортировок:
# ● Быстрая сортировка
# ● Сортировка слиянием

#       Быстрая сортировка
# “Программирование это разбиение чего-то большого и невозможного на что-то маленькое и
# вполне реальное”
# Быстрая сортировка принадлежит такой стратегии, как “разделяй и властвуй”.
#ПРИМЕР: Иван загадал число 77.
# Петр: Число больше 50? Иван: Да.
# Петр: Число больше 75? Иван: Да.
# Петр: Число больше 87? Иван: Нет.
# Петр: Число больше 81? Иван: Нет.
# Петр: Число больше 78? Иван: Нет.
# Петр: Число больше 76? Иван: Да
# Число оказалось в диапазоне 76 < x < 78, значит это число 77. Задача решена. На самом деле мы
# сейчас познакомились с алгоритмом бинарного поиска, который также принадлежит стратегии
# “разделяй и властвуй”. Давайте перейдем к обсуждению программного кода быстрой
# сортировки.

# def quicksort(array):
#     if len(array) < 2:
#         return array
#     else:
#         pivot = array[0]
#         less = [i for i in array[1:] if i <= pivot]
#         greater = [i for i in array[1:] if i > pivot]
#         return quicksort(less) + [pivot] + quicksort(greater)
# print(quicksort([10, 5, 2, 3]))

#Сортировка Слиянием
# def merge_sort(nums): # функция упорядовачиня списка
#     if len(nums) > 1:
#         mid = len (nums) //2
#         left = nums [:mid]
#         right = nums [mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i=j=k=0
#         while i < len (left) and j <len(right):
#             if left[i] < right [j]:
#                 nums[k] = left[i]
#                 i+=1
#             else:
#                 nums[k] = right[j]
#                 j+=1
#             k+=1

#         while i < len(left):
#             nums[k] = left[i]
#             i+=1
#             k+=1
#         while j < len(right):
#             nums[k] = right[j]
#             j+=1
#             k+=1

# list1=[1,23,45,32,56,3,6,43,423,2345]
# merge_sort(list1)
# print(list1)