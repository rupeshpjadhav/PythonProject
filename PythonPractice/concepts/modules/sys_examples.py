# sys module
# The sys module gives access to values and functions tied to the Python interpreter.
# It is useful for reading command-line input, checking the environment, and controlling how the program exits.

import sys

# Python version information
# sys.version is a long string with the full version and build details.
print(sys.version)
# version_info is a named tuple, so you can read the major and minor numbers separately.
print(sys.version_info.major, sys.version_info.minor)

# Command-line arguments
# When you run: python sys_examples.py hello world
# sys.argv looks like ['sys_examples.py', 'hello', 'world']
# Index 0 is always the script name. Everything after it is something the user typed.
print("Script name:", sys.argv[0])
print("Arguments:", sys.argv[1:])

# Module search path (where Python looks for imports)
# sys.path is a list of folders Python searches when you write "import something".
# Index 0 is usually the folder that holds the script being run.
print(sys.path[0])

# Checking the platform
# sys.platform names the operating system the program is running on.
print(sys.platform)     # 'darwin' on macOS, 'win32' on Windows, 'linux' on Linux

# Size of an object in memory (bytes)
# getsizeof() reports the memory used by one object. It does not include objects it refers to.
print(sys.getsizeof([1, 2, 3]))

# Maximum integer size used for indexing
# maxsize is the largest value Python uses for container sizes and indexes on this platform.
print(sys.maxsize)

# Exiting the program with a status code
# A status code of 0 means success. Any other number tells the shell that something went wrong.
# Calling sys.exit() stops the program immediately, so any code after it does not run.
# sys.exit(0) ends the program successfully
# sys.exit(1) ends the program with an error code
if len(sys.argv) < 2:
    print("No extra arguments were given.")
