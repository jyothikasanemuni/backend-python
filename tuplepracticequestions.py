# 1. Create a tuple with 5 elements and print it.
a=(1,2,3,4,5)
print(a)
# 2. Access the third element of a tuple.
a=(1,2,3,4,5)
print(a[2])
# 3. Slice a tuple to get the first 3 elements.
a=(1,2,3,4,5)
print(a[:3])
# 4. Check if an item exists in a tuple.
a=(1,2,3,4,5,6,7,8)
if 6 in a:
    print("number 6 is present")
else:
    print("number 6 is not present")
# 5. Concatenate two tuples.
a1=(1,2,3,4,5)
a2=(6,7,8,9,10)
x=a1+a2
print(x)
# 6. Repeat a tuple three times.
a=(1,2,3)
x=a*3
print(x)
# 7. Find the length of a tuple.
a=(1,2,3,4,5)
print(len(a))
# 8. Convert a list into a tuple.
list=(1,2,3,4,5)
print(type(list))
# 9. Convert a tuple into a list.
x=[1,2,3,4]
print(type(x))
# 10. Find the index of an element in a tuple.
a=(1,2,3,4,5,6,7)
x=a.index(5)
print(x)
# 11. Count occurrences of an element in a tuple.
a=(1,2,3,4,1,3,2,1,6,3,7,4,2)
print(a.count(1))
# 12. Create a nested tuple and access inner elements.
a=(1,2,(3,4),5)
tuple=a.index(3)
print(tuple)
# 13. Check if all elements in a tuple are integers.

# 14. Unpack a tuple into variables.
a, b, c = (10, 20, 30)
print(a, b, c)
# 15. Swap values of two variables using a tuple.
a=(1,2)
b=(5,6)
a,b=b,a
print("the tuple of a is:",a,"the tuple of b is:",b)
# 16. Iterate through a tuple using a loop.
a=(1,2,3,4,5,6,7,8,9)
for i in a:
    print(i)
# 17. Find the max and min values in a numeric tuple.
a=(1,2,3,4,5,6,7,8,9,10)
print("the max number is:",max(a))
print("the min number is:",min(a))
# 18. Sort elements of a tuple (convert and sort).
my_tuple=(1,9,2,3)
print(tuple(sorted(my_tuple)))
# 19. Merge tuples of equal length into pairs.
t1 = (1, 2, 3)
t2 = ('a', 'b', 'c')
print(tuple(zip(t1,t2)))

# 20. Create a tuple of even numbers using range().
for i in range(0,100):
    if i%2==0:
        print(i)