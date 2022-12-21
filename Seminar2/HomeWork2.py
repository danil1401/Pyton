
# 14. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11
# Решить через строку

# num =abs(float(input('Write number: ')))            # abs функция преобразования в положительное число
# sum=0
# for i in str(num):
#     if i!='.' or i!=',':
#         sum+=int(i)
# print(sum)
    
# 15. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# num=int(input(' Write number: '))
# prods=[1]
# print(prods)
# for i in range(2, num+1):
#     prods.append(prods[i-2]*i)
# print(prods)

# 16. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
#         Сумма 9.06

# num=int(input('Введите число: '))
# seq={}
# seq_sum=0
# for i in range(1, num+1):
#     seq[i]=round((1+1/i)**i,2)
# print(f'Для N={num}{seq}')
# print(f'Сумма {sum(seq.values())}')

# 17. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
# import random
# num =int(input('Введите число: '))
# my_list=[]
# for i in range(num):
#     my_list.append(random.randint(-num,num))
# print(my_list)

# with open ('file.txt','w') as data:# as datat -закрывает работу с файлом
#     data.write('1\n')
#     data.write('2\n')
#     data.write('3\n')

# path='file.txt'
# data=open(path,'r')
# mult=1
# for line in data:
#     mult*=my_list[int(line)]
# print(mult)


# 18. Реализуйте алгоритм перемешивания списка.
import random
a=[1,2,3,4,5,6,7,8]
random.shuffle(a)
print(a)