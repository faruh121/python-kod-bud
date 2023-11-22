# print("Hello")
# print("Hello","world","hi")
# print()
# print('A'=='a')
# n = input("Как тебя зовут ?")
# print("Привет",n)
# import random
# rand = random.randint(1,40)
# atem = 3
# print("Угадай число от 1 до 40 у вас 3 попытки")
# while True:
#     if atem>0:
#         q = int(input("Введи число: "))
#         if q == rand:
#             print("Угадал!")
#             print("Попытки - ",atem)
#             break
#         elif q!=rand:
#             print("не угдал , попробуй еще)")
#             atem-=1
#             print("Попытки - ",atem)
#     else:
#         print("Попытки кончились!")
#         break

# v = int (input("Введите ширину прямоугольника:"))
# s = int (input("Введите высоту прямоугольника:"))
# print("Площадь - ", v*s)
# print("Периметр - ", 2*(v+s))





# while n!=0:
#     n = int(input("Введите вашу температуру а программа скажет \nздоров\nнизкая\nвысокая: "))
#     if n<36.6:
#         print("Низкая температура")
#     elif n>36.6:
#         print("Высокая температура")
#     else:
#         print("Нормальная")
# else:
#     print("Ты мертв(")

# n = int(input("Введите число: "))
# print('Chet' if n%2==0 else 'Nechet')


# n = int(input("Введите число: "))
# print("-" if n>100 or n<-100 else "+")


# a = int(input("Введите 1  число: "))
# b = int(input("Введите 2 число: "))
# c = int(input("Введите 3 число: "))
# print("Yes" if a>10 and b>10 and c>10 else "No")

# #перебор стррооки
# word = 'Hello my name is'
# for i in word:
#     print(i)

# #Конкатенация строк 
# print(f'{word} oleg')

# #Длинна строки 
# print(len(word))

# #проверка вхождений в строку 
# if word=='Hello' or word=='hello':
#     print("Приветствие найденно!")

# #Умножение строки на число
# print(word*3)

#Поиск элемеента по индексу где 0 это первый элемент 1 второй и тд так же чтобы выводить с конца нужно начинать с -1
# s = 'PUthon'
# print(s[-1])

#Перебор элементов если нужен индекс())()()()()
# for i in range(len(s)):
#     print(s[i])
# for x in s:
#     print(x)



#срезы again....

#x[x:y] x start y end

# s = 'abcdefghij'
# print(s[2:5])
# print(s[0:6])
# print(s[2:7])


#function
# def name_function(parametr):
#     block_cod


# class urokFunction:
#     def risFunc(self):
#         for i in range(5):
#             print('*' *7)
# n = urokFunction()
# n.risFunc()
    


# def risFunct(h,w):
#     for i in range(h):
#         print('*' *w)
# risFunct(h=12,w=12)


# #Локальные и глобальные переменные
# x=5
# def locl():
#     global x #как менять переменную в функции
#     x+=1
# print(x) #Локальная переменная
# locl()#ГЛобальная переменная

# #Функции возращающие значения 
# def func():
#     x = 5
#     x+=10
#     return(x)
# result = func()
# print(result)
# print(func())



# def ploshad(a,b):
#     s= a*b
#     return s
# print(ploshad(a=12,b=12))

# #после ретурна нельзя писать дальше код работате по типу  брейка


# #lambda function
# res = lambda x: x+55
# print(res(4))


# res_1 = lambda x,y:x+y
# print(res_1(4,5))





def pramougol(a,b):
    s = a*b
    p = a+b+a+b
    print(f'Периметр -  {p} Площадь - {s}')
pramougol(4,5)

x = int(input("введите год: "))
def chekgod(a):
    if (a%4==0 and a%100==1) or (a%400==0):
        print("Весокосный")
    else:
        print("Не вескосный")
chekgod(a=x)










