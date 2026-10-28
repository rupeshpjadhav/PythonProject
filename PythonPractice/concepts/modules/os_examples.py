# os module
# The os module lets Python interact with the operating system:
# working with directories, file paths, environment variables, and more.
# All file operations below run inside a temporary folder so your project stays clean.

import os
import tempfile

# Information about the current system and working directory
# os.name tells you the operating system family: 'posix' covers macOS and Linux, 'nt' covers Windows.
print(os.name)              # 'posix' on macOS/Linux, 'nt' on Windows
# getcwd() returns the folder the program is running from (its "current working directory").
print(os.getcwd())          # current working directory
# os.sep is the separator used between folders in paths. Windows uses a backslash.
print(os.sep)               # path separator: '/' on macOS/Linux, '\\' on Windows

# Environment variables
# Environment variables are settings stored by the operating system (for example, your home folder path).
# os.environ behaves like a dictionary of these values.
home = os.environ.get("HOME", "not set")   # .get() avoids an error if the variable is missing; "not set" is the default
print(f"Home folder: {home}")
# Changing os.environ only affects this program and any child processes it starts.
os.environ["MY_SETTING"] = "demo"          # set a variable for this program
print(os.getenv("MY_SETTING"))             # 'demo' (getenv works like .get() on os.environ)

# Creating a temporary folder to work in
# mkdtemp() creates a new, uniquely named folder in the system's temp location and returns its path as a string.
base_dir = tempfile.mkdtemp()
print("Working in:", base_dir)

# Joining paths safely (works on every operating system)
# os.path.join() adds the correct separator for your OS, so you never hard-code "/" or "\\".
folder = os.path.join(base_dir, "demo_folder")
# makedirs() creates a folder and any missing parent folders in between.
# exist_ok=True stops it from raising an error if the folder already exists.
os.makedirs(folder, exist_ok=True)         # creates nested folders, no error if it exists

# Creating and writing a file
# open(..., "w") creates the file, or replaces it if it already exists.
# The "with" block closes the file automatically, even if an error happens inside it.
file_path = os.path.join(folder, "notes.txt")
with open(file_path, "w") as f:
    f.write("Hello from the os module!")

# Checking paths
# exists() is True for both files and folders. isfile() and isdir() check which one it is.
print(os.path.exists(file_path))    # True
print(os.path.isfile(file_path))    # True
print(os.path.isdir(folder))        # True

# Splitting paths
# basename() returns the last part of the path (the file name).
print(os.path.basename(file_path))  # notes.txt
# dirname() returns everything before the last part (the folder).
print(os.path.dirname(file_path))   # the folder that contains notes.txt
# splitext() separates the extension from the rest of the path. It returns a tuple.
print(os.path.splitext(file_path))  # ('.../notes', '.txt')

# File information
# getsize() returns the file size in bytes.
print(os.path.getsize(file_path))   # size in bytes

# Listing folder contents
# listdir() returns the names (not full paths) of everything directly inside a folder.
print(os.listdir(folder))           # ['notes.txt']

# Walking through a folder tree
# os.walk() visits a folder and every sub-folder inside it.
# For each folder it yields: the current path (root), a list of sub-folder names (dirs), and a list of file names (files).
for root, dirs, files in os.walk(base_dir):
    for name in files:
        print("Found file:", os.path.join(root, name))

# Renaming and removing
# rename() moves or renames a file or folder. The old path stops existing afterwards.
new_path = os.path.join(folder, "renamed.txt")
os.rename(file_path, new_path)
print(os.listdir(folder))           # ['renamed.txt']

# remove() deletes a single file. It does not work on folders.
os.remove(new_path)                 # delete a file
# rmdir() deletes a folder, but only if it is empty. Otherwise it raises an error.
os.rmdir(folder)                    # delete an empty folder
print("Folder cleaned up:", not os.path.exists(folder))

# Remove the temporary base folder we created
os.rmdir(base_dir)

# Running a shell command (use with care)
# system() runs a command in the operating system's shell and returns its exit code.
# Avoid passing untrusted input to it, because the input could run unwanted commands.
# os.system("echo Hello from the shell")
