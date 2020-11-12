# # declare a list witth numbers 1 - 5 and add 6 at the end of the list 
# num_list = [1,2,3,4,5]
# print(num_list)
# num_list.append(6)
# print(num_list)

# # create  a tuple  with values 1 - 5
# my_tuple = 1,2,3,4,5
# print(my_tuple)
# # can you append to this? NO 

# # print tuple up to number 3
# my_tuple = 1,2,3,4,5
# print(my_tuple[0:3]) # not it's not inclusive of the last index, so this only prints to index number 2

# # declare a dictionary of a shopping list
# shopping_list = {
#     'fruits': 5.00,
#     'eggs' : 2.50,
#     'veg' : 8.99
# }
# print(type(shopping_list))

# # print the price of the third item 
# print(shopping_list['veg'])

# # replace the price of the third item 

# shopping_list['veg'] = 10.99
# print(shopping_list)

# # write a funciton which adds two arguments
# def add(a,b):
#     return a + b

# # create a class called person with name and age
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# person_instance = Person('Farah',22)
# print(person_instance.age)
# print(person_instance.name)

# # # create a class called Student and inherit everything from the parent class (Person)
# # class Student(Person):
# #     def __init__(self,name,age,student_id, course):
# #         super().__init__(self)
# #         self.student_id = student_id
# #         self.course = course
    
# # student_instance = Student('Farah', 22, 1234, 'DevOps')
# # print(student_instance.name, student_instance.age, student_instance.student_id, student_instance.course)

# # # 

# create a dict with 4 items shoppint items with prices 
my_dict = {
    'bread': 1.00,
    'eggs': 2.50,
    'fruits':3.00,
    'chicken': 3.50
}
print(my_dict)

print(my_dict['bread'] + my_dict['eggs'] + my_dict['fruits'] + my_dict['chicken'])

# define super class and provide a usecase 
# the super() method allows one to access attributes and methods from the parent class

# Task 10
# add kiwi at index 3
my_dict['kiwis'] = 3
print(my_dict)

# declare a list with your shopping items from ur dict
shopping_list = ['chicken','bread','eggs','fruits']
for item in shopping_list:
    if item == 'chicken':
        print(item)