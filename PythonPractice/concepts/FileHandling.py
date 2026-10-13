import os

# File handling is used to read data from files and save data to files.
# It is important for working with logs, configuration files, reports, and user data.
# Common modes are:
# 'r' - read mode
# 'w' - write mode (overwrites the file)
# 'a' - append mode (adds to the end)
# 'r+' - read and write mode

# Opening a file.
# file = open("example.txt", "r")
# content = file.read()
# print(content)
# file.close()

# Reading from files
# read() reads the entire file as a single string.
# readline() reads one line at a time.
# readlines() reads all lines and returns them as a list of strings.
file = open("example.txt", "r")
file.seek(0)
lines = file.readlines()
print(lines)
file.close()

# Writing to a file
# 'w' creates a new file or overwrites an existing one.
# 'a' adds data without deleting existing data.
with open("output.txt", "w") as file:
    file.write("Hello, this is a test.\n")
    file.write("Python file handling is easy!")

# Example of safe file handling using try/except.
try:
    file = open("nonexistent.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found! Please check the file path.")
finally:
    if 'file' in locals() and not file.closed:
        file.close()

# Delete a file using the os module.
os.remove("output.txt")

# Notes:
# - Always close files after use when using open().
# - The with statement is preferred because it closes files automatically.
# - Use read() for small files and readlines() for line-by-line processing.

