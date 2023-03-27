# УСКОРЕННАЯ ОБРАБОТКА ДАННЫХ: LAMBDA, FILTER, MAP, ZIP, ENUMERATE,LIST,COMPREHENSION

#                                                       Анонимные, Lambda функции:

# def sum(x):
#     return x+10

# def sum1(x):
#     return x+22

# def sum3(x):
#     return x+242

# def mult(x):
#     return x**2

# def mult2(x):
#     return x**3

# def mult4(x):
#     return x**5

# sum(mult(2))
# sum2(mult2(2))
# sum3(mult2(2))

#Пример
# def f(x): #функция возводит х во вторую степень
#     x**2
# print(type(f)) #type выдает Тип функции-в данном случае это функция

#Пример:
# def f(x):
#     return x**2

# g=f #присваиваем переменной g функцию f, т.е это переменная которая хранит в себе ссылку на функцию// вывод получается одинаковый
# print(f(2))
# print(g(2))

# Пример:
# def calc1(x):
#     return x+10
# print(calc1(10))

# def calc2(x):
#     return x*10
# # print(calc2(10))

# def math(op, x):
#     print(op(x))

# math(calc2,10)

#Пример с 2мя переменными:
# def sum(x,y):
#     return x+y
# f=sum
# #или лучше (тоже самое что и функция выше)
# sum=lambda x,y: x+y

# def mylt(x,y):
#     return x*y
# d=mylt

# def calc(op,a,b): # op это аргумент(можно назвать по разному) в нем можно хранить целую функцию (можно указать любую функцию)
#     print(op(a,b))

# calc(f,4,5)# тоже самое что и calc(mylt,4,5), т.к f=функции sum
# calc(sum,6,9)#используется функция sum с lambda
# #либо можно сделать напрямую-избавиться от переменной sum и пробросить сразу lambda
# calc(lambda x,y: x+y,8,2)

# calc(d,10,13)

#                                                        List Comprehension
# нужен он для того что бы быстро создавать списки

# [exp for item in iterable]
# [exp for item in iterable (if conditional)]
# [exp <if conditional> for item in iterable (if conditional)]

#Пример (создать четный список от 1 до 100)
# list=[]

# for i in range(1,101):
#     if(i%2==0):
#         list.append(i)
# print(list)
# #Преобразуем данный пример:
# list=[]

# for i in range(1,101):
#     if(i%2==0):
#         list.append(i)
# print(list)

# list= [i for i in range(1,21) if i%2==0]# получаем то же самое что и код выше)
# #list= [(i,i) for i in range(1,21) if i%3==2]# делаем список кортежей
# print(list)

#Пример в сочетании с функцией:
def f(x):
    return x**3
list= [f(i) for i in range(1,21) if i%2==0]# добавили функцию f, где i четное число возведенное в степень согласно условию функции
list= [(i,f(i)) for i in range(1,21) if i%2==0]# добавили кортеж, где будет указано число и его куб(согласно условию функции)
print(list)

# продолжить с 20:55