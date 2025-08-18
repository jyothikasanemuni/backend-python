#CASE CONVERSIONS INBUILT FUNCTIONS OF STRINGS#
a="Jyothika Sanemuni"
a=a.lower()      #lower : converting the characters into lower (small alphabets)
print("The lower string is:",a)
a=a.upper()      #upper :converting the characters into capitals
print("the upper string string is: ",a)

x="jyothika"
x=x.isupper()   #is upper :checking the string given characters are upper or not
print("checking the string is upper or not:",x)
a="JyothikA"
a=a.islower()   #islower :checking the string given characters are lower or not
print("checking the string is lower or not:",a)

a="JyOtHiKa SaneMUNI"
a=a.swapcase()  #swapcase: converts the characters upper to lower and lower to upper
print(a)

a="jYOTHIKA"
a=a.capitalize()  #capitalize: first ltter in the string capital, rest are smalls.
print(a)

a="jyothika sanemuni"
a=a.title() #title: converting the first letter and after the spaces are capitals
print(a)

# TRIMMING INBUILT FUNCTIONS
# to remove the spaces in a string we use strip()
a="     jyothika      "
a=a.strip()  #strip(): removing spaces in the string
print(a)

a="     jyothika      "
a=a.rstrip()  #rstrip(): removing right side spaces in the string
print(a)

a="     jyothika      "
a=a.lstrip()   #lstrip(): removing left side spaces in the string
print(a)

#replacing words
a="i am a java developer"
a=a.replace("java","python")
print(a)

a="bailey is playing"
a=a.replace("playing","sleeping")
print(a)

#SEARCHING AND FINDING FUNCTIONS
a="jyothika"
a=a.find("a")  # finding the character using find()
print(a)

a="jyothika"
a=a.find("b")  # finding not present character using find() output=-1
print(a)

a="There is a lizard on the wall"
a=a.rfind("a") # finding the character from right
print(a)

a="There is a lizard on the wall"
a=a.rfind("a",0,16) # finding the character from right in blw the indexes 0-16
print(a)
#count()
a="It's raining outside"
a=a.count("n")
print(a)
#index():
a="jyothika"
a=a.index("a")
print(a)
a="jyothika"
a=a.index("b")   #valueerror: substring not found
print(a)        # diff b/w find and index is if the character is not present in the find() it returns (-1) in  index() it returns value error.....
