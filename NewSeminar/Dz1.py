# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# number=int(input('Введите 3 цифры: '))
# if 100<=number<=999:
# sum_of_number=number%10+number//10%10+number//100
# print(sum_of_number)
# else:
# print('Введено не верно')

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

# sum=int(input('Сколько всего сделано журавликов? '))
# part=sum//3
# peter=serj=part//2
# kate=2*peter*2

# print(f'Катя сделала {kate} журавликов, Петя {peter} и Сережа {serj} журавликов')

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

# number=input('Введите номер билета: ')
# if int(number[0])+int(number[1])+int(number[2])==int(number[3])+int(number[4])+int(number[5]):
# print("Билет счастливый")
# else:
# print('Билет обычный')

## или
# n=int(input('Введите номер билета : ' ))
# n123=n//1000
# n456=n%1000

# sum123=0
# sum456=0

# while n123>0:
# sum123+=n123%10
# n123//=10
# while n456>0:
# sum456+=n456%10
# n456//=10
# if sum123==sum456:
# print('Билет счастливый')
# else:
# print('Билет обычный')


# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

# n=int(input('Длина шоколадки в дольках: '))
# m=int(input('Ширина шоколадки в дольках: '))
# k=int(input('Количество долек для отлома: '))

# if(k%m==0 or k%n==0) and k<n*m and k>0:
# print("Такое количество долек можно отломить за один разлом")
# else:
# print('Такое количество долек нельзя отломить за один разлом')