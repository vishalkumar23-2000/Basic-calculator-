# -*- coding: utf-8 -*-
"""Copy of basic calculator

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uFZmaLSJsLousKMkk0YvGveoT8iX0u9P
"""

# Function to add two numbers.
def add(a,b):
# (a,b) both are variables to store values.
    return a + b

# Function to subtract two numbers.
def subtract(a,b):
    return a - b

# Function to multiply two numbers.
def multiply(a,b):
    return a * b

# Functions to divide two numbers.
def divide(a,b):
    if b != 0:
      return a / b
    else:
      return"cannot divide by zero"

# Main function
def main():
    print("Simple calculator")
    print("Operations")
    print("Add")
    print("Subtract")
    print("Multiply")
    print("divide")

choice = input("Enter the operation number (1-4):")

num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number"))

if choice == '1':
    print("Result:", add (num1, num2))

if choice == '2':
    print("Result:", subtract(num1, num2))

if choice == '3':
    print("Result:", multiply(num1, num2))

if choice == '4':
    print("Result:", divide(num1, num2))

else:
    print("Invalid input")

if __name__ == "__main__":
    main()

############# Three Variable #############

# Function to add two numbers.
def add(a,b,c):
# (a,b) both are variables to store values.
    return a + b + c

# Function to subtract two numbers.
def subtract(a,b,c):
    return a - b - c

# Function to multiply two numbers.
def multiply(a,b,c):
    return a * b * c

# Function to add three numbers.
def add(a,b,c):
# (a,b) both are variables to store values.
    return a + b + c

# Function to subtract three numbers.
def subtract(a,b,c):
    return a - b - c

# Function to multiply three numbers.
def multiply(a,b,c):
    return a * b * c

# Functions to divide three numbers.
def divide(a,b,c):
    if b != 0 and c != 0:
      return a / b / c
    else:
      return"cannot divide by zero"

# Main function
def main():
    print("Simple calculator")
    print("Operations")
    print("Add")
    print("Subtract")
    print("Multiply")
    print("divide")

    choice = input("Enter the operation number (1-4):")

    num1 = float(input("Enter the first number:"))
    num2 = float(input("Enter the second number"))
    num3 = float(input("Enter the third number"))

    if choice == '1':
        print("Result:", add (num1, num2, num3))

    elif choice == '2':
        print("Result:", subtract(num1, num2, num3))

    elif choice == '3':
        print("Result:", multiply(num1, num2, num3))

    elif choice == '4':
        print("Result:", divide(num1, num2, num3))

    else:
        print("Invalid input")

if __name__ == "__main__":
    main()
