# pathlib module
# pathlib is the modern, object-oriented way to work with file paths.
# Instead of plain strings, paths are Path objects with handy methods.
# All file operations below run inside a temporary folder so your project stays clean.
# Path objects work on every operating system, so you do not need to think about "/" vs "\\".

from pathlib import Path
import tempfile

# Creating Path objects
# Path.cwd() returns the current working directory as a Path object.
current = Path.cwd()          # current working directory
print(current)
# Path.home() returns your user's home folder (for example, /Users/yourname on macOS).
print(Path.home())           # your home folder

# Building paths with / (no need for os.path.join)
# Path(...) turns a string into a Path. tempfile.mkdtemp() gives us a fresh folder to work in.
base_dir = Path(tempfile.mkdtemp())
# The / operator joins path pieces. It is the pathlib way of writing os.path.join().
folder = base_dir / "demo_folder"
file_path = folder / "notes.txt"
print(file_path)

# Creating folders
# mkdir() creates a folder. parents=True also creates any missing folders above it.
# exist_ok=True prevents an error if the folder is already there.
folder.mkdir(parents=True, exist_ok=True)   # parents=True creates missing parent folders

# Writing and reading text files
# write_text() creates the file (or overwrites it) and writes the string in one step.
# encoding="utf-8" makes sure special characters like accents and emoji are saved correctly.
file_path.write_text("Hello from pathlib!", encoding="utf-8")
# read_text() opens the file, reads everything, and returns it as one string.
print(file_path.read_text(encoding="utf-8"))

# Checking paths
# exists() is True for files and folders. is_file() and is_dir() check which one it is.
print(file_path.exists())     # True
print(file_path.is_file())    # True
print(folder.is_dir())        # True

# Parts of a path
# These properties read the different pieces of a path without any string splitting.
print(file_path.name)         # notes.txt (the full file name)
print(file_path.stem)         # notes (the name without the extension)
print(file_path.suffix)       # .txt (the extension, including the dot)
print(file_path.parent)       # the folder that contains notes.txt
print(file_path.parts)        # tuple of every part of the path, starting from the root

# Changing the file name or extension
# with_name() returns a new Path with a different file name. The original file is not renamed.
renamed = file_path.with_name("renamed.txt")
print(renamed.name)           # renamed.txt
# with_suffix() returns a new Path with a different extension. Again, nothing on disk changes.
print(file_path.with_suffix(".md").name)   # notes.md (only the name changes here)

# File size
# stat() returns file information. st_size holds the size in bytes.
print(file_path.stat().st_size, "bytes")

# Listing files with a pattern
# glob("*.txt") finds matching items in the current folder only.
# rglob("*.txt") finds matching items in the folder and all of its sub-folders.
for txt_file in base_dir.rglob("*.txt"):    # rglob searches sub-folders too
    print("Found:", txt_file.name)

# Iterating over a folder
# iterdir() yields every item directly inside a folder, both files and sub-folders.
for item in folder.iterdir():
    print("Item:", item.name)

# Copying content to another file and renaming
# read_bytes() and write_bytes() copy raw data. This works for any file type, not just text.
copy_path = folder / "copy.txt"
copy_path.write_bytes(file_path.read_bytes())
# sorted() puts the names in alphabetical order so the output is predictable.
print(sorted(p.name for p in folder.glob("*")))   # ['copy.txt', 'notes.txt']

# Cleaning up
# unlink() deletes a file. rmdir() deletes an empty folder. Both raise an error if the target is not in the expected state.
copy_path.unlink()            # delete a file
file_path.unlink()
folder.rmdir()                # delete an empty folder
base_dir.rmdir()
print("Cleaned up:", not base_dir.exists())
