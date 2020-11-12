# declare a list with numbers 1-5 and add 6 to end

# list = [1, 2, 3, 4, 5]
# print(list)
# list.append(6)
# print(list)

# create a tuple 1-5

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(type(my_tuple))

num_set = {1, 2, 3, 4, 5}

for number in num_set:
    if number <= 3:
        print(number)
    else:
        break
