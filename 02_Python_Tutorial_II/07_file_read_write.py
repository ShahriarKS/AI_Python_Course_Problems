# Problem: Write text to a file and read it.

filename = "sample.txt"

with open(filename, "w") as file:
    file.write("Hello Python File Handling!
")

with open(filename, "r") as file:
    content = file.read()

print(content)
