'''1'''

# class Student:
#     def __init__(self, name, age, mark):
#         self.name = name
#         self.age = age
#         self.mark = mark
# student = Student('Bob', 13, 5)
# print(student.name, student.age, student.mark)

'''2'''
# class Student:
#     def __init__(self, name, age, mark):
#         self.name = name
#         self.age = age
#         self.mark = mark
#     def say_info(self):
#         print(f"Имя: {self.name}, Возраст: {self.age}, Средний балл: {self.mark}")
# student = Student('Bob', 13, 5)
# print(student.name, student.age, student.mark)
# student.say_info()

'''3'''
# class Student:
#     def __init__(self, name, age, mark):
#         self.name = name
#         self.age = age
#         self.mark = mark
#     def say_info(self):
#         print(f"Имя: {self.name}, Возраст: {self.age}, Средний балл: {self.mark}")

# class Students(Student):
#     def __init__(self, name, age, mark, name_diplom):
#         super().__init__(name, age, mark)
#         self.__name_diplom = name_diplom  
#     def get_name_diplom(self):
#         return self.__name_diplom


# student = Student('Bob', 13, 5)
# students = Students('Mark', 18, 3, 'eco')
# print(student.name, student.age, student.mark)
# student.say_info()
# students.get_name_diplom()

'''4'''
# class Human:
#     def __init__(self, gender, height):
#         self.gender = gender
#         self.height = height
# class Student(Human):
#     def __init__(self, gender, height, name, age, mark):
#         super().__init__(gender, height)
#         self.name = name
#         self.age = age
#         self.mark = mark
#     def say_info(self):
#         print(f"Имя: {self.name}, Возраст: {self.age}, Средний балл: {self.mark}")

# class Students(Student, Human):
#     def __init__(self, gender, height, name, age, mark, name_diplom):
#         super().__init__(gender, height, name, age, mark)
#         self.__name_diplom = name_diplom  
#     def get_name_diplom(self):
#         return self.__name_diplom

# human = Human('male', 185)
# student = Student('male', 170, 'Bob', 13, 5)
# students = Students('male', 190, 'Mark', 18, 3, 'eco')
# print(student.gender, student.height, student.name, student.age, student.mark)
# print(students.gender, students.height, students.name, students.age, students.mark)
# print(human.gender, human.height)
# student.say_info()
# students.get_name_diplom()