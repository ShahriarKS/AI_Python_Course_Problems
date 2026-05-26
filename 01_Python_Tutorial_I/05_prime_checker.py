# Problem: Check whether a number is prime.

n = int(input("Enter a number: "))

if n <= 1:
    print("Not Prime")
else:
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    print("Prime" if is_prime else "Not Prime")
