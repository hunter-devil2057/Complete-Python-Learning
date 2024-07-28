# Operators in Python 
    # 1. Arithmetic Operators: +, -, *, /, etc. 
    # 2. Assignment Operators: ++, --, =, +=, -=
    # 3. Comparison Operators: ==, >=, <=, !=, >, <
    # 4. Logical Operators: and, or, not
    
# 1. Arithmetic Operators: 
a=34
b=10
sum=a+b
difference=a-b
product=a*b
quotient=a/b
print("Sum=",sum)
print("Difference", difference)
print("Product=",product)
print("Quotient", quotient)

# 2. Assignment Operators: 
c=4-2   #Assigning 4-2 in c
d=6
print("d=", d)
d+=3    #Increment the value of b by 4 and then assign it to b
print("d+=3: ",d)
# d=6+3=9
d-=5
# d=9-5=4
print("d-=5: ", d)

# 3. Comparison Operators
e=5>20
print("5>20: ", e)

f=5<20
print("5<20: ", f)

g=5==5
print("5==20: ", g)


# 4. Logical Operators
h=True or False
print(h)
print("Truth Table of OR")
print("True or False is: ", True or False)
print("True or True is: ", True or True)
print("False or True is: ", False or True)
print("False or False is: ", False or False)

print("Truth Table of AND")
print("True and False is: ", True and False)
print("True and True is: ", True and True)
print("False and True is: ", False and True)
print("False and False is: ", False and False)

print("Truth Table of NOT")
print("Not of True is: ", not(True))
print("Not of False is: ", not(False))