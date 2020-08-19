msg = "Hello World"

print(msg)
age = 8


print('{0} {1}'.format(msg, age))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # list
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)  # tuple
dictionary = {"first": 1, "second": 2}  # dict


for x, y in dictionary.items():  # python3 way to print out dict and loop
    print(x, y)
