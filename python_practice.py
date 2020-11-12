# declare a list with numbers 1-5 and add 6 to end

# list = [1, 2, 3, 4, 5]
# print(list)
# list.append(6)
# print(list)

# create a tuple 1-5

# my_tuple = (1, 2, 3, 4, 5)
# print(my_tuple)
# print(type(my_tuple))

# num_set = {1, 2, 3, 4, 5}
#
# for number in num_set:
#     if number <= 3:
#         print(number)
#     else:
#         break

# declare a dictionary of a shopping list with three items
# dictionary = {"items": ("bread", "garlic bread", "baguette"), "price": ("1", "3", "5")}
# print(dictionary)
# print(type(dictionary))
# print(dictionary["price"])

# append item in dictionary
# dictionary_2 = {"items": "bread", "price": "1"}
# dictionary_2["price"] = "5"
# print(dictionary_2)

# function to add 2 numbers
# def add(num1, num2):
#     return num1 + num2

# Create a class called person with name and age

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# me = Person("Ben", 22)
# print(me.name)
# print(me.age)

# Inherit person into new class student
# class Student(Person):
#     def __init__(self, name, age, student_id, course):
#         super().__init__(name, age) # super method is used to inherit from the parent class to access its attributes and methods
#         self.student_id = student_id
#         self.course = course
#
#
# student = Student("Ben", 22, 1, "devops")
# print(student.name, student.age,student.student_id, student.course)

# create a dictionary and add the item values
# new_dictionary = {"bread": 4, "garlic bread": 5, "baguette": 6, "egg": 7}
# print(new_dictionary)
# print(type(new_dictionary))
# new_dictionary["big bread"] = 8
# # this will add big bread to the last index in the list
# print(new_dictionary)

# print(sum(new_dictionary.values()))

# function to do the same
# def sum_items():
#     return print(sum(new_dictionary.values()))
#
# sum_items()

my_list = ["hi", "hello", "hey", "greetings"]
for i in my_list:
    if i == "hello":
        break
    print(i)





