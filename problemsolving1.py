#1. Print reverse of a string(without built in function).
string="jyothika"
for i in str:
    x=str[::-1]
print(x)
# 2. Average of marks of five students   marks=[400, 450, 530, 550, 570]
marks=[400, 450, 530, 550, 570]
for i in marks:
    avg=sum(marks)/len(marks)
print(avg)
# 3 check whether the given sides form a triangle or not:a=5, b=5, c=5 (Triangle rule: sum of any two sides is greater than the third side)
a,b,c=5,5,5
if a+b>c or b+c>a or c+a>b:
        print("the three sides are equal it is a triangle")
else:
        print("not a triangle")
