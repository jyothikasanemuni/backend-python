
#Create a list of 5 integers.
list=[1,2,3,4,5]
print(list)
#Access the 3rd element of a list.
list=[1,2,3,4,5]
print(list[2])
#Change the value at index 2.
list=[1,2,3,4,5]
list[2]=9
print(list)
#Append an element to the list.
list=[1,2,3,3]
list.append(10)
print(list)
#Insert an element at index 1.
list=[10,20,30,40,50]
list.insert(1,60)
print(list)
#Remove an element by value.
list=[1,2,3,1,3]
list.remove(3)
print(list)
#Remove an element by index.
list=[1,2,3,6,7,8]
list.pop(3) #removing the element with index value 6 index value is 3
print(list)
#Find the length of a list.
list={1.223,234,2.34231,4435,345456,4564623,4534536688,35,79}
print(len(list))
#Check if an element exists in a list.
list=["apple","mango","banana","guava","pineapple"]
if "apple" in list:
    print("apple is present")

#Loop through a list and print each item.
list=[1,2,3,4,5,6,7,8,9,10]
for i in list:
    print(i)

#Sort a list in descending order.
list=[21,76,23,75,98,34,24,53,27,106,53,62]
list.sort(reverse=True)     #reverse=True it sorts the list in descending order
print("Descending order is:", list)
#Sort a list in ascending order.
list=[21,76,23,75,98,34,24,53,27,106,53,62]
list.sort()    #default the reverse is false so it sorts the list in ascending order
print("Ascending order is:", list)

#Reverse a list using reverse().
list=[1,2,3,4,23,154,34,76,78,90,12]
list.reverse()
print(list)
#Reverse a list using slicing.
list=[1,2,3,4,23,154,34,76,78,90,12]
reverse=list[::-1]
print(reverse)

#Copy a list using slicing.
list=[1,2,3,31,31,23,13]
copy_list=list[:]
print()
#Copy a list using the copy() method.
list=[1,2,3,4,5]
list=list.copy()
print(list)
#Clear all elements in a list.
list1=[1,2,3,4,4]
list.clear()
print(list)
#Count occurrences of a number.
list=[1,2,3,2,3,5,3,4,4,5,2,4]
print(list.count(2))
#Find the index of a number.
list=[1,2,3,4,5,6]
list=list.index(5)
print(list)
#Concatenate two lists.
list1=[1,2,3]
list2=[4,5,6]
list=list1+list2
print(list)