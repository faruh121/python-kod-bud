# Написать модуль с функциями суммы, вычитания, умножения, деления.

# В основном файле создать консольную программу калькулятор и воспользоваться для расчета функциями из модуля.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Деление на ноль недопустимо")
    
'''
from atestatmodule2 import *

def calculator_program():
    print("Калькулятор")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    choice = input("Выберите операцию (1-4): ")

    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    if choice == '1':
        result = atestatmodule2.add(num1, num2)
        print("Результат сложения:", result)
    elif choice == '2':
        result = atestatmodule2.subtract(num1, num2)
        print("Результат вычитания:", result)
    elif choice == '3':
        result = atestatmodule2.multiply(num1, num2)
        print("Результат умножения:", result)
    elif choice == '4':
        try:
            result = atestatmodule2.divide(num1, num2)
            print("Результат деления:", result)
        except ValueError as e:
            print("Ошибка:", e)
    else:
        print("Неверный выбор операции")

calculator_program()
в одном модуле тк нельзя загружать 2 файла на сайт

'''