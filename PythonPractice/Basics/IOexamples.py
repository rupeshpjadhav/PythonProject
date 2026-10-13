# File I/O Example in Python
# File handling allows us to store data outside the program so it can be reused later.
# We can create a file, write text into it, read its content, and append more content.
# Using the with statement is a good practice because Python closes the file automatically.

# Writing to a file using 'w' mode.
# 'w' creates a new file or overwrites an existing file.
with open('D:\\development\\PythonPractice\\IOexamples.txt', 'w') as file:
    file.write("This is my new file to learn Python programming\n")
    file.write("This is the second line of the file\n")
    file.write("This is the third line of the file\n")

# Appending to a file using 'a' mode.
# 'a' adds new content at the end without deleting existing content.
with open('D:\\development\\PythonPractice\\IOexamples.txt', 'a') as file:
    file.write("This is the fourth line of the file\n")
    file.write("This is the fifth line of the file\n")
    file.write("This is the sixth line of the file\n")

# Reading the entire file content using read().
with open('D:\\development\\PythonPractice\\IOexamples.txt', 'r') as file:
    content = file.read()
    print(content)

# Reading one line at a time using readline().
# This is useful when processing a file line by line.
with open('D:\\development\\PythonPractice\\IOexamples.txt', 'r') as file:
    line = file.readline()

    while line:
        if line.strip():
            print(line, end='')
        line = file.readline()

# Notes:
# - read() reads the whole file at once.
# - readline() reads a single line.
# - readlines() reads all lines and returns them as a list.
# - The with statement is preferred because it automatically closes the file.

