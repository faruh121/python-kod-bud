# Реализовать родительский класс человека, а также дочерние классы директора, преподавателя и ученика. Описать для каждого класса необходимые свойства и методы.



# Важно: директор помимо своих обязанностей может также и преподавать (множественное наследование).

# class school:
#     def __init__(self,age,name,obazon,rank):

#         self.name = name
#         self.age = age
#         self.obazon = obazon
#         self.rank = rank

# class student(school):
#     def __init__(self,age,name,obazon,rank):
#         super().__init__(age,name,obazon,rank)
# class teacher(school):
#     def __init__(self,age,name,obazon,rank):
#         super().__init__(age,name,obazon,rank)
# class Administration(school):
#     def __init__(self,age,name,obazon,rank):
#         super().__init__(age,name,obazon,rank)


# stud_name = student(name='Василий',age=15,obazon='Учиться',rank='Ученик')
# Tiuter_name = teacher(name='Иван',age=25,obazon='Учить',rank='Учитель')
# Admin_name = Administration(name='Алеша',age=55,obazon='Учить , управлять школой',rank='Директор')

# print(f'Здравствуйте, меня зовут - {stud_name.name}, мне {stud_name.age} лет, я {stud_name.rank} и я обязан {stud_name.obazon}')
# print(f'Здравствуйте, меня зовут - {Tiuter_name.name}, мне {Tiuter_name.age} лет, я {Tiuter_name.rank} и я обязан {Tiuter_name.obazon}')
# print(f'Здравствуйте, меня зовут - {Admin_name.name}, мне {Admin_name.age} лет, я {Admin_name.rank} и я обязан {Admin_name.obazon}')