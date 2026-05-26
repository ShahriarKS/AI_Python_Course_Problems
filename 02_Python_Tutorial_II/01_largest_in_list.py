# Problem: Find largest element from a list.

numbers = [10, 5, 30, 22, 8]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest:", largest)
