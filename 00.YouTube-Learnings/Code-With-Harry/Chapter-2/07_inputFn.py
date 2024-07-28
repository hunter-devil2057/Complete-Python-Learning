# Input Function,
# input(): allows the user to take input formthe keyboard as a string
# By Default, they take string as their input
a=input("Enter First String: ")
b=input("Enter Second String: ")

print("First String:", a)
print("Second String: ", b)

print("Enter Inputs Again: ")

name=input("Enter your Name: ")     #taking string input
age=int(input("Enter your Age: "))  # taking integer input
address=input("Enter your Address: ")   #taking string input 
salary=float(input("Enter your Salary: "))  #taking float input

# Displaying Information
print("Hi!, ", name, ". Nice to have you here...")
# Here, , concatenates the outputs while displaying on the screen. 
print("You're ", age, "years old")
print("So, you recently live in", address)
print("And, your monthly salary is: Rs. ", salary)