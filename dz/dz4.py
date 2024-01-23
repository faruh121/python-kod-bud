class myclass:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        print("Сложение:")
        return self.value + other.value

    def __sub__(self, other):
        print("Вычитание:")
        return self.value - other.value

    def __mul__(self, other):
        print("Умножение:")
        return self.value * other.value

    def __truediv__(self, other):
        print("Деление:")
        return self.value / other.value



a = myclass(10)
b = myclass(2)

print(a + b)
print(a - b)
print(a * b) 
print(a / b)  