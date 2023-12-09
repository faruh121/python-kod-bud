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





# def pramougol(a,b):
#     s = a*b
#     p = a+b+a+b
#     print(f'Периметр -  {p} Площадь - {s}')
# pramougol(4,5)

# x = int(input("введите год: "))
# def chekgod(a):
#     if (a%4==0 and a%100==1) or (a%400==0):
#         print("Весокосный")
#     else:
#         print("Не вескосный")
# chekgod(a=x)


# circl = [-2,3,10]
# #[x,y,r] or [r,x,y]
# def func():
#     pass


# class Test:
#     pass


# print(type(5))
# print(type('a'))
# print(type(5.5))
# print(type(True))
# print(type({1:2}))
# print(type([1,2]))
# print(type((1,2)))
# print(type(func))
# print(type(Test))



# class Person:
#     name='Ваня'
#     age = 12
#     def say(self):
#         print("Hello")

# person1 = Person()
# print(person1.name)
# person1.say()    



# person2 = Person()
# person2.name = 'Arkadiy'
# print(person2.name)



# class Person:
#     def __init__(self,name,age):
#         self.name = name 
#         self.age = age
#         #return f'Меня зовут{self.name}'
# #MEtod init
# person1 = Person(name='Ivan',age=15)
# person2 = Person(name='Petr',age=14)
# print(person1.age)
# print(person1.name)
# print(person2.age)
# print(person2.name)
# print(person1)
# print(person1)





# class Transport:
#     def __init__(self,speed,color) :
#         self.speed = speed
#         self.color = color

#     def beep(self):
#         print('beep')

# class Car(Transport):
#     def __init__(self, speed, color,owner):
#         self.owner = owner
#         super().__init__(speed, color)
#     def sayowner(self):
#         print(f'Владелец:{self.owner}')
# car1 = Car(speed=100,color='red',owner='Василий')
# print(car1.color)    
# print(car1.speed)    
# print(car1.owner)
# car1.beep()
# car1.sayowner()


# class bus(Transport):
#     def __init__(self, speed, color,seets):
#         super().__init__(speed, color)
#         self.seets =seets
#     def sayseet(self):
#         print(f'Кол - во мест{self.seets}')

# bus1 = bus(speed=100,seets=20,color='white')
# bus1.sayseet()



# class Sportcar(Car,Transport):
#     pass

# car1 = Sportcar(speed=200,color='red',owner='Maks')
# car1.beep()
# car1.sayowner()

#Написать класс ученика класса.Описать все возможные свойства которые можно обобщить для каждого ученика так же сохадть немного методов


# class student:
#     def __init__(self,name,age,clas):

#         self.clas= clas
#         self.name = name
#         self.age = age
#     def sayotm(self):
#         print("Я ничего не сделал(")
#     def sayops(self):
#         print("Здарвствуйте извините за опоздание")

# stud1 = student(name="Василий",age=12,clas=6)
# stud2 = student(name="Максим",age=13,clas=6)
# stud3 = student(name="Иван",age=11,clas=6)
# stud4 = student(name="Алексей",age=12,clas=6)



# print(stud1.name,stud1.age,stud1.clas)
# print(stud2.name,stud2.age,stud2.clas)
# print(stud3.name,stud3.age,stud3.clas)
# print(stud4.name,stud4.age,stud4.clas)

# stud1.sayops()
# stud1.sayotm()




#Реализовать род класс человека ,а также дочерние классы деректора преподорватели и ученика
class school:
    def __init__(self,age,name,obazon,rank):

        self.name = name
        self.age = age
        self.obazon = obazon
        self.rank = rank

class student(school):
    def __init__(self,age,name,obazon,rank):
        super().__init__(age,name,obazon,rank)
class teacher(school):
    def __init__(self,age,name,obazon,rank):
        super().__init__(age,name,obazon,rank)
class Administration(school):
    def __init__(self,age,name,obazon,rank):
        super().__init__(age,name,obazon,rank)


stud_name = student(name='Василий',age=15,obazon='Учиться',rank='Ученик')
Tiuter_name = teacher(name='Иван',age=25,obazon='Учить',rank='Учитель')
Admin_name = Administration(name='Алеша',age=55,obazon='Учить , управлять школой',rank='Директор')

print(f'Здравствуйте, меня зовут - {stud_name.name}, мне {stud_name.age} лет, я {stud_name.rank} и я обязан {stud_name.obazon}')
print(f'Здравствуйте, меня зовут - {Tiuter_name.name}, мне {Tiuter_name.age} лет, я {Tiuter_name.rank} и я обязан {Tiuter_name.obazon}')
print(f'Здравствуйте, меня зовут - {Admin_name.name}, мне {Admin_name.age} лет, я {Admin_name.rank} и я обязан {Admin_name.obazon}')
    
        







