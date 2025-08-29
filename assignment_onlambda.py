
# Basic Level
#  1 Square of a Number: Write a lambda function to find the square of a number. Example: square(5) → 25 
sq= lambda x:x**2
print(sq(5))
# 2 Check Even or Odd: Use lambda to check if a number is even or odd. Example: is_even(4) → True 
even_or_odd= lambda x: x%2==0
print(even_or_odd(3))
print(even_or_odd(6))
# 3 Find Maximum of Two Numbers: Write a lambda to return the larger of two numbers. Example: max_num(10, 20) → 20
maximum= lambda x,y: x if x>y else y
print(maximum(2,3))
#  4 Add Two Numbers: Write a lambda function that takes two arguments and returns their sum. Example: add(4, 6) → 10
total=lambda x,y:x+y
print(total(2,4))

#  Intermediate Level
#  1 Sort a List of Tuples: Given [(1, 5), (2, 3), (4, 1)], sort the list by the second element using lambda.
list1=[(1, 5), (2, 3), (4, 1)]
sorting=sorted(list1, key=lambda t:t[1] ) #sorting the second element in the list like 5,3,1 --> 1,3,5
print(sorting)
#  2 Filter Even Numbers: Use filter() with a lambda to extract even numbers from [1,2,3,4,5,6,7,8,9,10]. 
listt=[1,2,3,4,5,6,7,8,9,10]
evens=list(filter(lambda x:x%2==0 ,listt))
print(evens)
# 3 Map with Lambda: Use map() and lambda to cube each number in [1, 2, 3, 4, 5].
list2=[1, 2, 3, 4, 5]
cubes=tuple(map(lambda x:x**3,list2))
print(cubes)
#  4 Reduce with Lambda: Use reduce() and lambda to find the product of [2, 3, 4, 5].
from functools import reduce
list3=[2, 3, 4, 5]
product=reduce(lambda x,y:x*y,list3)
print(product)

#  Advanced Level 
# 1 Sort by Name Length: Given ["apple", "banana", "kiwi", "grapes"], sort by length using sorted() and lambda.
list=["apple", "banana", "kiwi", "grapes"]
sorting=sorted(list, key=lambda w:len(w), reverse=True) #in default it is false
print(sorting)
#  2 Find Palindromes: Use filter() with lambda to find palindromes from ["madam", "python", "level", "world"]. 
palin=["madam", "python", "level", "world"]
palindrome=set(filter(lambda x:x==x[::-1] ,palin))
print(palindrome)
# 3 Custom Sorting (Case-Insensitive): Sort ["Cat", "apple", "Banana", "dog"] in case-insensitive order using lambda.
pets=["Cat", "apple", "Banana", "dog"] 
sorting_pets=sorted(pets, key=lambda x:x.lower())
print(sorting_pets)
#  4 Conditional Lambda (Ternary): Write a lambda function that returns "Positive", "Negative", or "Zero" based on input. 
num=int(input("enter a number: "))
number=lambda x:"positive" if x>0 else("negative" if x<0 else "0")
print(number(num))
# 5 Dictionary Sorting by Values: Given {'a': 3, 'b': 1, 'c': 2}, sort dictionary items by values using lambda.
dict1={'a': 3, 'b': 1, 'c': 2}
sorting=sorted(dict1.items(),key=lambda x:x[1]) #sort the second elements(values) like 3,2,1 ---> 1,2,3
print(sorting)
#  6 Multiple Conditions in Lambda: Write a lambda to return: 'Even & >10' if number is even and greater than 10, 'Odd' if odd, 'Other' otherwise
num = int(input("Enter a number: "))
check = lambda x: "Even & >10" if (x % 2 == 0 and x > 10) else ("Odd" if x % 2 != 0 else "Other")
print(check(num))
