# Problem: Generate Fibonacci series using function.

def fibonacci(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

n = int(input("How many terms? "))
print(fibonacci(n))
