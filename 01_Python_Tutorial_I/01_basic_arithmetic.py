# Problem: Take two numbers as input and print sum, subtraction, multiplication, and division.

def calculate(a, b):
    print("Sum:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    if b != 0:
        print("Division:", a / b)
    else:
        print("Division not possible by zero")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
calculate(a, b)
