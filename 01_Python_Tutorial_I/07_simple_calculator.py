# Problem: Simple calculator using if-else.

a = float(input("First number: "))
op = input("Operator (+, -, *, /): ")
b = float(input("Second number: "))

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print(a / b if b != 0 else "Cannot divide by zero")
else:
    print("Invalid operator")
