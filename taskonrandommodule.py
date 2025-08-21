
# 1. Generate a random float between 0.0 and 1.0. 
import random
print(random.random())

# 2. Generate a random integer between 1 and 100. 
import random
print(random.randint(1,100))

# 3. Pick a random fruit from a list ["apple", "banana", "mango", "orange"]. 
list=["apple", "banana", "mango", "orange"]
print(random.choice(list))

# 4. Shuffle a list of numbers [1, 2, 3, 4, 5]. 
list1=[1, 2, 3, 4, 5]
print(random.sample(list1, k=5))

# 5. Generate 5 random integers between 10 and 50
import random
list=[]
for i in range(5):
    var=random.randint(10,50)
    list.append(var)
print(list)

    





