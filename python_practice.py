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

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


me = Person("Ben", 22)
# print(me.name)
# print(me.age)


class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course


student = Student("Ben", 22, 1, "devops")
print(student.name, student.age,student.student_id, student.course)
