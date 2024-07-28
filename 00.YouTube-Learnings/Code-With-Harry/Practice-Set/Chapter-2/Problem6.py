# Write a python program to calculate the square of a number entered by the user.

# Asking Input from the user
num=int(input("Enter a number: "))

# operation to calculate square of number
# square=pow(num, 2)        #we can use this as well
# power of num raised to the power 2

# square=num*num        #we can use this as well

square=num**2       #we can use this as well
# num raised to the power 2

# displaying the output
print("Square of ", num, "is: ", square)