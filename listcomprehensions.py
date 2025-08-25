# # a=[10,20,30,40,50]
# sum=0
# for i in a:
#     sum+=i
# print(sum)
# #sum using lisst comprehension
# l=[1,2,3]
# total=sum([i for i in l])
# print(total)
# #power
# a=1
# b=6
# power=[i**2 for i in range(a,b)]
# print(power)
# #without list comprehension
# a=[1,2,3]
# n=[]
# for i in a:
#     b=i**2
#     n.append(b)
# print(n)
# #dict without comprehension
# a=6
# dict={}
# for i in range(a):
#     if i%2==0:
#      dict[i]="even"
#     else:
#      dict[i]="odd"
# print(dict)
# #dict with comprehension
# l={i:i*i for i in range(1,7)}
# print(l)

# print vowels in a str without list comprehension
# a="comprehensions"
# v=[]
# for i in a:
#   if i in "aeiou":
#     v.append(i)
# print(v)
#with comprehension 
s="comprehensions"
d=[i for i in s if i in "aeiou"]
print(d)
# # create a list of numbers form 1-10
# l=[numbers for numbers in range(1,11)]
# print(l)

# #create a list of squares of numbers form 1-10
# a=[num**2 for num in range(1,11)]
# print(a)

# #from a list [2,3,4,5,6,7,8] create a new list with only even values.
# li=[2,3,4,5,6,7,8]
# b=[i for i in li if i%2==0 ] #even numbers are already stored here in b so no need for append.
# print(b)

# # From a string "python", make a list of all characters.
# string="python"
# c=[list for list in string]
# print(c)

# # Create a list of numbers from 1 to 20 that are divisible by 3.
# a=[nums for nums in range(1,21) if nums%3==0]
# print(a)

# # From the list ["apple", "banana", "cherry", "kiwi", "mango"],
# # create a new list containing only fruits with the letter 'a'.
# list=["apple", "banana", "cherry", "kiwi", "mango"]
# fruits=[i for i in list if "a" in i]
# print(fruits)
# # From the same fruits list, create a new list with fruits whose length > 5.
# list=["apple", "banana", "cherry", "kiwi", "mango"]
# l=[ch for ch in list if len(ch)>5]
# print(l)
# # Convert every fruit name into uppercase.
# list=["apple", "banana", "cherry", "kiwi", "mango"]
# l=[m.upper() for m in list]
# print(l)
# # Create a list of the first letter of each fruit.
# list=["apple", "banana", "cherry", "kiwi", "mango"]
# l=[i[0] for i in list ]
# print(l)
# # Create a list of cubes of numbers from 1 to 10, but only include odd numbers.
# l=[i**3 for i in range(1,11) if i%2!=0]
# print(l)

# # Generate a list of tuples (x, y) where x is from [1, 2, 3] and y is from [4, 5, 6].
# x=[1,2,3]
# y=[4,5,6]
# l=[(i,j) for i in x for j in y]
# print(l)

# # Flatten this nested list [[1,2], [3,4], [5,6]] into [1,2,3,4,5,6].
# a=[[1,2], [3,4], [5,6]]
# l=[j for i in a for j in i]
# print(l)
# # Create a list of all vowels from the string "List Comprehensions are Powerful".
# str="List Comprehensions are Powerful"
# l=[i for i in str if i in "aeiou"]
# print(l)

# # Generate a list of numbers from 1 to 100 that are prime numbers.
# # Create a dictionary {n: n**2} for numbers from 1 to 5 using comprehension.
# l={i:i**2 for i in range(1,6)}
# print(l)
