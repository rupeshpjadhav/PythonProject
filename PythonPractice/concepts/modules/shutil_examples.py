# shutil module
# shutil ("shell utilities") offers higher-level file operations than os:
# copying files and whole folders, moving them, deleting folder trees, and checking disk space.
# All file operations below run inside a temporary folder so your project stays clean.

import os
import shutil
import tempfile

# Creating a temporary working area
# mkdtemp() makes a unique folder in the system temp location and returns its path as a string.
base_dir = tempfile.mkdtemp()
source_dir = os.path.join(base_dir, "source")
os.makedirs(source_dir)

# Creating a sample file to work with
with open(os.path.join(source_dir, "notes.txt"), "w") as f:
    f.write("Hello from shutil!")

# Copying a file
# copy() copies file contents and permission bits. The destination can be a file path or a folder.
# If the destination is a folder, the copy keeps the original file name.
copy_path = shutil.copy(os.path.join(source_dir, "notes.txt"), base_dir)
print("Copied to:", copy_path)

# copy2() works like copy() but also keeps metadata such as the last-modified time.
backup_path = shutil.copy2(os.path.join(source_dir, "notes.txt"), os.path.join(base_dir, "notes_backup.txt"))
print("Backup created:", backup_path)

# Copying a whole folder tree
# copytree() copies a folder and everything inside it, including sub-folders.
# The destination folder must not exist yet. Otherwise it raises an error.
tree_copy = os.path.join(base_dir, "source_copy")
shutil.copytree(source_dir, tree_copy)
print("Folder copied:", os.listdir(tree_copy))

# Moving a file or folder
# move() renames a file or folder when the destination is in the same drive.
# If the destination is in another drive, it copies the item and then deletes the original.
moved_path = shutil.move(backup_path, os.path.join(base_dir, "moved_backup.txt"))
print("Moved to:", moved_path)

# Disk usage
# disk_usage() returns a named tuple with total, used, and free space, in bytes.
usage = shutil.disk_usage(base_dir)
print(f"Free space: {usage.free // (1024 ** 3)} GB")   # // is integer division, so the result is whole gigabytes

# Finding an executable on the system PATH
# which() returns the full path to a command if it can be found, or None if it cannot.
print("Python location:", shutil.which("python3"))

# Creating an archive (zip)
# make_archive() creates a zip file from a folder. The first argument is the output name without the extension.
archive_path = shutil.make_archive(os.path.join(base_dir, "source_archive"), "zip", source_dir)
print("Archive created:", os.path.basename(archive_path))

# Extracting an archive
# unpack_archive() extracts the zip into the folder given as the second argument.
extract_dir = os.path.join(base_dir, "extracted")
shutil.unpack_archive(archive_path, extract_dir)
print("Extracted files:", os.listdir(extract_dir))

# Removing a folder tree
# rmtree() deletes a folder and everything inside it. There is no undo, so be careful with the path.
# os.rmdir() can only delete empty folders, but rmtree() handles nested contents too.
shutil.rmtree(base_dir)
print("Cleaned up:", not os.path.exists(base_dir))
