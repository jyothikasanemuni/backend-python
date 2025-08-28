# Python Beginner Tasks on enumerate() and zip()
# Tasks on enumerate()

# Task 1: Simple Index Printing
# Write a program to print each item in the list along with its index using enumerate().
fruits = ["apple", "banana", "cherry"]
for index,fruit in enumerate(fruits):
    print(f"{index} {fruit}")

# Task 2: Start Index from 1
# Use enumerate() with start=1 to display serial numbers for a list of student names.
students = ["Alice", "Bob", "Charlie"]
for serial_numbers,names in enumerate(students,start=1):
    print(f"{serial_numbers} {names}")

# Task 3: Replace for with enumerate()
# Re-write this loop using enumerate():
# colors = ["red", "green", "blue"]
# index = 0
# for color in colors:
#     print(index, color)
#     index += 1
colors = ["red", "green", "blue"]
for index,color in enumerate(colors):
    print(f"{index} {color}")

# Task 4: Find Index of a Specific Value
# Using enumerate(), find the index of "python" in this list:
languages = ["java", "c++", "python", "ruby"]
for index,langs in enumerate(languages):
    if langs=="python":
        print("index of python is:",index)

# Task 5: Enumerate on a String
# Use enumerate() to print each character of the string "hello" with its index.
string="hello"
for index,str in enumerate(string):
    print(f"{index} {str}")

# Tasks on zip()
# Task 6: Combine Two Lists
# Use zip() to pair elements from these lists:
# names = ["Alice", "Bob", "Charlie"]
# marks = [85, 90, 78]
# Expected Output:
# ("Alice", 85), ("Bob", 90), ("Charlie", 78)
names = ["Alice", "Bob", "Charlie"]
marks = [85, 90, 78]
pair=(zip(names,marks))
for i in pair:
    print(i)

# Task 7: Iterate with zip()
# Write a program that prints sentences like:
# Alice scored 85
# Bob scored 90
# Charlie scored 78
names = ["Alice", "Bob", "Charlie"]
marks = [85, 90, 78]
for nms,scores in zip(names,marks):
    print(f"{nms} scored {scores}")

# Task 8: Unzipping
# Given:
# pairs = [("a", 1), ("b", 2), ("c", 3)]
# Use zip(*pairs) to separate keys and values.
pairs = [("a", 1), ("b", 2), ("c", 3)]
i,j=zip(*pairs)
print("keys:",i)
print("values:",j)

# Task 9: Multiple Iterables
# Use zip() on three lists:
# ids = [101, 102, 103]
# names = ["Tom", "Jerry", "Mickey"]
# grades = ["A", "B", "A"]
# Expected Output:
# (101, "Tom", "A")
# (102, "Jerry", "B")
# (103, "Mickey", "A")
ids = [101, 102, 103]
names = ["Tom", "Jerry", "Mickey"]
grades = ["A", "B", "A"]
triple=(zip(ids,names,grades))
for i in triple:
    print(i)


# Task 10: Shortest List Behavior
# Check how zip() behaves when given lists of different lengths:
# a = [1, 2, 3, 4]
# b = ["x", "y"]
a = [1, 2, 3, 4]
b = ["x", "y"]
for vals,vars in zip(a,b):
    print(f"{vals} {vars}") #only  gives 2 vals bcoz there sre only 2 vars...
