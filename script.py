# # # print("Hello")
# # # print("Hello","world","hi")
# # # print()
# # # print('A'=='a')
# # # n = input("Как тебя зовут ?")
# # # print("Привет",n)
# # # import random
# # # rand = random.randint(1,40)
# # # atem = 3
# # # print("Угадай число от 1 до 40 у вас 3 попытки")
# # # while True:
# # #     if atem>0:
# # #         q = int(input("Введи число: "))
# # #         if q == rand:
# # #             print("Угадал!")
# # #             print("Попытки - ",atem)
# # #             break
# # #         elif q!=rand:
# # #             print("не угдал , попробуй еще)")
# # #             atem-=1
# # #             print("Попытки - ",atem)
# # #     else:
# # #         print("Попытки кончились!")
# # #         break

# # # v = int (input("Введите ширину прямоугольника:"))
# # # s = int (input("Введите высоту прямоугольника:"))
# # # print("Площадь - ", v*s)
# # # print("Периметр - ", 2*(v+s))





# # # while n!=0:
# # #     n = int(input("Введите вашу температуру а программа скажет \nздоров\nнизкая\nвысокая: "))
# # #     if n<36.6:
# # #         print("Низкая температура")
# # #     elif n>36.6:
# # #         print("Высокая температура")
# # #     else:
# # #         print("Нормальная")
# # # else:
# # #     print("Ты мертв(")

# # # n = int(input("Введите число: "))
# # # print('Chet' if n%2==0 else 'Nechet')


# # # n = int(input("Введите число: "))
# # # print("-" if n>100 or n<-100 else "+")


# # # a = int(input("Введите 1  число: "))
# # # b = int(input("Введите 2 число: "))
# # # c = int(input("Введите 3 число: "))
# # # print("Yes" if a>10 and b>10 and c>10 else "No")

# # # #перебор стррооки
# # # word = 'Hello my name is'
# # # for i in word:
# # #     print(i)

# # # #Конкатенация строк 
# # # print(f'{word} oleg')

# # # #Длинна строки 
# # # print(len(word))

# # # #проверка вхождений в строку 
# # # if word=='Hello' or word=='hello':
# # #     print("Приветствие найденно!")

# # # #Умножение строки на число
# # # print(word*3)

# # #Поиск элемеента по индексу где 0 это первый элемент 1 второй и тд так же чтобы выводить с конца нужно начинать с -1
# # # s = 'PUthon'
# # # print(s[-1])

# # #Перебор элементов если нужен индекс())()()()()
# # # for i in range(len(s)):
# # #     print(s[i])
# # # for x in s:
# # #     print(x)



# # #срезы again....

# # #x[x:y] x start y end

# # # s = 'abcdefghij'
# # # print(s[2:5])
# # # print(s[0:6])
# # # print(s[2:7])


# # #function
# # # def name_function(parametr):
# # #     block_cod


# # # class urokFunction:
# # #     def risFunc(self):
# # #         for i in range(5):
# # #             print('*' *7)
# # # n = urokFunction()
# # # n.risFunc()
    


# # # def risFunct(h,w):
# # #     for i in range(h):
# # #         print('*' *w)
# # # risFunct(h=12,w=12)


# # # #Локальные и глобальные переменные
# # # x=5
# # # def locl():
# # #     global x #как менять переменную в функции
# # #     x+=1
# # # print(x) #Локальная переменная
# # # locl()#ГЛобальная переменная

# # # #Функции возращающие значения 
# # # def func():
# # #     x = 5
# # #     x+=10
# # #     return(x)
# # # result = func()
# # # print(result)
# # # print(func())



# # # def ploshad(a,b):
# # #     s= a*b
# # #     return s
# # # print(ploshad(a=12,b=12))

# # # #после ретурна нельзя писать дальше код работате по типу  брейка


# # # #lambda function
# # # res = lambda x: x+55
# # # print(res(4))


# # # res_1 = lambda x,y:x+y
# # # print(res_1(4,5))





# # # def pramougol(a,b):
# # #     s = a*b
# # #     p = a+b+a+b
# # #     print(f'Периметр -  {p} Площадь - {s}')
# # # pramougol(4,5)

# # # x = int(input("введите год: "))
# # # def chekgod(a):
# # #     if (a%4==0 and a%100==1) or (a%400==0):
# # #         print("Весокосный")
# # #     else:
# # #         print("Не вескосный")
# # # chekgod(a=x)


# # # circl = [-2,3,10]
# # # #[x,y,r] or [r,x,y]
# # # def func():
# # #     pass


# # # class Test:
# # #     pass


# # # print(type(5))
# # # print(type('a'))
# # # print(type(5.5))
# # # print(type(True))
# # # print(type({1:2}))
# # # print(type([1,2]))
# # # print(type((1,2)))
# # # print(type(func))
# # # print(type(Test))



# # # class Person:
# # #     name='Ваня'
# # #     age = 12
# # #     def say(self):
# # #         print("Hello")

# # # person1 = Person()
# # # print(person1.name)
# # # person1.say()    



# # # person2 = Person()
# # # person2.name = 'Arkadiy'
# # # print(person2.name)



# # # class Person:
# # #     def __init__(self,name,age):
# # #         self.name = name 
# # #         self.age = age
# # #         #return f'Меня зовут{self.name}'
# # # #MEtod init
# # # person1 = Person(name='Ivan',age=15)
# # # person2 = Person(name='Petr',age=14)
# # # print(person1.age)
# # # print(person1.name)
# # # print(person2.age)
# # # print(person2.name)
# # # print(person1)
# # # print(person1)





# # # class Transport:
# # #     def __init__(self,speed,color) :
# # #         self.speed = speed
# # #         self.color = color

# # #     def beep(self):
# # #         print('beep')

# # # class Car(Transport):
# # #     def __init__(self, speed, color,owner):
# # #         self.owner = owner
# # #         super().__init__(speed, color)
# # #     def sayowner(self):
# # #         print(f'Владелец:{self.owner}')
# # # car1 = Car(speed=100,color='red',owner='Василий')
# # # print(car1.color)    
# # # print(car1.speed)    
# # # print(car1.owner)
# # # car1.beep()
# # # car1.sayowner()


# # # class bus(Transport):
# # #     def __init__(self, speed, color,seets):
# # #         super().__init__(speed, color)
# # #         self.seets =seets
# # #     def sayseet(self):
# # #         print(f'Кол - во мест{self.seets}')

# # # bus1 = bus(speed=100,seets=20,color='white')
# # # bus1.sayseet()



# # # class Sportcar(Car,Transport):
# # #     pass

# # # car1 = Sportcar(speed=200,color='red',owner='Maks')
# # # car1.beep()
# # # car1.sayowner()

# # #Написать класс ученика класса.Описать все возможные свойства которые можно обобщить для каждого ученика так же сохадть немного методов


# # # class student:
# # #     def __init__(self,name,age,clas):

# # #         self.clas= clas
# # #         self.name = name
# # #         self.age = age
# # #     def sayotm(self):
# # #         print("Я ничего не сделал(")
# # #     def sayops(self):
# # #         print("Здарвствуйте извините за опоздание")

# # # stud1 = student(name="Василий",age=12,clas=6)
# # # stud2 = student(name="Максим",age=13,clas=6)
# # # stud3 = student(name="Иван",age=11,clas=6)
# # # stud4 = student(name="Алексей",age=12,clas=6)



# # # print(stud1.name,stud1.age,stud1.clas)
# # # print(stud2.name,stud2.age,stud2.clas)
# # # print(stud3.name,stud3.age,stud3.clas)
# # # print(stud4.name,stud4.age,stud4.clas)

# # # stud1.sayops()
# # # stud1.sayotm()




# # #Реализовать род класс человека ,а также дочерние классы деректора преподорватели и ученика
# # class school:
# #     def __init__(self,age,name,obazon,rank):

# #         self.name = name
# #         self.age = age
# #         self.obazon = obazon
# #         self.rank = rank

# # class student(school):
# #     def __init__(self,age,name,obazon,rank):
# #         super().__init__(age,name,obazon,rank)
# # class teacher(school):
# #     def __init__(self,age,name,obazon,rank):
# #         super().__init__(age,name,obazon,rank)
# # class Administration(school):
# #     def __init__(self,age,name,obazon,rank):
# #         super().__init__(age,name,obazon,rank)


# # stud_name = student(name='Василий',age=15,obazon='Учиться',rank='Ученик')
# # Tiuter_name = teacher(name='Иван',age=25,obazon='Учить',rank='Учитель')
# # Admin_name = Administration(name='Алеша',age=55,obazon='Учить , управлять школой',rank='Директор')

# # print(f'Здравствуйте, меня зовут - {stud_name.name}, мне {stud_name.age} лет, я {stud_name.rank} и я обязан {stud_name.obazon}')
# # print(f'Здравствуйте, меня зовут - {Tiuter_name.name}, мне {Tiuter_name.age} лет, я {Tiuter_name.rank} и я обязан {Tiuter_name.obazon}')
# # print(f'Здравствуйте, меня зовут - {Admin_name.name}, мне {Admin_name.age} лет, я {Admin_name.rank} и я обязан {Admin_name.obazon}')
    
        
# # #Аргументы по умолчанию

# # # def get_name(name='Ivan'):
# # #     print(name)
# # # get_name()
# # # get_name('Petr')


# # # class Car:
# # #     def __init__(self,speed,color='Yelow',owner=None) :
# # #         self.speed = speed
# # #         self.color = color
# # #         self.owner = owner
# # #     def sayowner(self):
# # #         if self.owner:
# # #             print(f'Владелец - {self.owner}')
# # #         else:
# # #             print('У автомобиля нету владельца!')

# # # car1 = Car(speed=100,color='green',owner='Иван')
# # # car2 = Car(speed=90,color='Blue')
# # # print(f'{car1.color=}{car2.color=}')

# # # car1.sayowner()
# # # car2.sayowner()


# # class Person:
# #     _age = 15
# #     def __say_hello(self):
# #         print('Привет!')
# # person1 = Person()
# # print(person1._age)
# # person1._age = 14
# # print(person1._age)
# # person1._Person__say_hello()

# # class Human:
# #     def __init__(self,name):
# #         self._name = name
# #     @property
# #     def name(self):
# #         return self._name
# #     @name.setter
# #     def name(self,value):
# #         self.name = value
    


# # person = Human('Ivan')
# # print(person.name)
# # person.name = 'Seregey' 



# class Parent:
#     def say_hello(self):
#         print('ПРивет я метод род класса!')

# class children(Parent):
#     def say_hello(self):
#         print('ПРивет я метод доч класса!')
# child = children()
# child.say_hello()    


# class Test(list):
#     def append(self,object) :
#         for i in range(len(self)):
#             self[i]**=object

# a =Test([1,2,3])
# print(a)
# a.append(2)
# print(a)



# class  Test_1:
#     def __str__(self):
#         return'Тест класс!'
# b = Test_1()
# print(b)


# class chto(int):
#     def __init__(self,num) -> None:
#         super().__init__()
#         self.num = num

#     def __add__(self, num2):
#         return self.num * num2
    
# a = chto(5)
# print(a+10)


# class Point2D:
#     '''Точка на плоскости
#     поле класса(доступна без создания экзэмпляров)
#     хранит кол-во экзэмпляров класса т является обще для всех объектов этого класса
#     '''

#     instanes_count = 0
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#         #При инстацировании уведичиваем кол во экзэмпляров класса
#         Point2D.instanes_count+=1

#         def __str__(self):
#             '''Вренуть строку в виде точка 2 д (х,у)'''
#             return f'ТОчка 2 д {self.x,self.y}'
#         def __add__(self,other):
#             #Сложить селф и отхер
#             #Параметры:
#             # - other(Point2D):Вернуть объект сумму
#             #еСЛИ INT OR FLOAT СДВИНУТЬ ТОЧКУ НА ОТЗЕР ПО Х У 
#             # - отхер другой тип возбудить исключение тайп еророр

#             if isinstance(other, self.__class__):
#                 #ТОчка с точкой
#                 #Возращает новый объект
#                 return Point2D(self.x+other.x,self.y+other.y)
#             elif isinstance(other, (int,float)):
#                 '''Точка и число
#                 добавим обим координатам селф число отхер и вернем результат
#                 Возвращаем старый измененный объект'''
#                 self.x +=other
#                 self.y +=other
#                 return self
#             else:
#                 '''В противном случае мы сгенерируем исключени'''
#                 raise TypeError(f'Не могу добавить {type(other)} к {self.__class__}')
#         def __sub__(self,other):
#             #СОздать новый объект как разность координат
#             return Point2D(self.x-other.x,self.y-other.y)
#         def __neg__(self):
#             return Point2D(-self.x,-self.y)
#         def __eq__(self,other):
#             return self.x==other.x,self.y==other.y
# n1 = Point2D(0,5)
# n2 = Point2D(-5,10)
# print(n1+n2)
# print(Point2D.instanes_count)


#МОдули
# from module import * 



#from name_module import *

#ТИпо калькулятор для модуля
# def add(num1: float,num2: float) ->float:
#     return num1 + num2
# def sub(num1: float,num2: float) ->float:
#     return num1 - num2
# def mul(num1: float,num2: float) ->float:
#     return num1 * num2
# def truediv(num1: float,num2: float) ->float:
#     return num1 / num2
# if __name__=='__main__':
#     print('Modul zapshen kak samostoatelnoa programa')
#     num1 = int(input('1 число:'))
#     num2 = int(input('2 число:'))
#     choice = int(input('Операция или выход:'))
#     match choice:
#         case 0:
#             print('ДЛя выхода интер')
#             input()
#         case 1:
#             print(add,(num1,num2))
#         case 2:
#             print(mul,(num1,num2))
#         case 3:
#             print(sub,(num1,num2))
#         case 4:
#             print(truediv,(num1,num2))
# # _name__ - Полное имя модуля # __doc__ - Строка документации # __dict_ - Словарь модуля
# # _file__ - Файл, в котором модуль определяется # __package__ - Имя содержащегося пакета (если он есть)
# __path__ - Список подкаталогов для поиска полмодулей пакета
# annotations__ - Аннотации типов уровня поиска
# my_package/
# init_
# i・Py
# primitive/
# __init_-py text.py line.py
# formats/
# __init__.py
# jpeg.py
# png-py
            
# полный путь
# import my_package.primitive.fill.func()
'''
match and case rabotout tipa if
'''



# num = [1,2,3,4]
# r = (x*x for x in num)
# print(r)
# for num in r:
#     print(num)

# print(next(r))
# print(next(r))

# numbers = [1, 2, 3, 4]
# result = (x * x for x in numbers)
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))

# for num in result:
#     print(num)


# f = open('test.txt')
# lines = (t.strip() for t in f)
# comments = (t for t in lines if t[0] == '#')
# for c in comments:
#     print(c)

# def func(num):
#    while num > 0:
#        yield num
#        num -= 1

# for num in func(5):
#    print(num)


# def func(num):
#    while num > 0:
#        yield num
#        num -= 1

# result = func(5)
# print(next(result))
# print(next(result))
# print(next(result))


# def func(num):
#    while num > 0:
#        yield num
#        num -= 1

# result = func(5)
# print(result.__next__())
# print(result.__next__())

# Задача 1 
# Числа Фибоначчи представляют последовательность, получаемую в результате сложения двух предыдущих элементов.  
# Начинается коллекция с чисел 1 и 11.  
# Она достаточно быстро растет, поэтому вычисление больших значений занимает немало времени.  
# Создайте функцию fib(n), генерирующую n чисел Фибоначчи с минимальными затратами ресурсов. 
# Для реализации этой функции потребуется обратиться к инструкции yield. 




# def fib(n):
#     a, b = 1, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b
# for num in fib(10):
#     print(num)





emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
      	'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
      	'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
      	'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
      	'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
      	'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}

print(sorted(f"{name}@{d}" for d, name in emails.items() for name in name))