# Problem: Remove duplicates from a list while keeping order.

items = [1, 2, 2, 3, 4, 4, 5]
unique = []

for item in items:
    if item not in unique:
        unique.append(item)

print(unique)
