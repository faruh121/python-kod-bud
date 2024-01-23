def check(n):
    if len(n) == len(set(n)):
        return True
    else:
        return False
    


'''Потом я вызову этот модуль вот так 

from dz5module import check


a = [1, 2, 3, 3, 4, 5]
result = check(a)
print(result) 

пишу так потому что на сайте нельзя загружать 2 файла
'''