import os
import shutil

# Define source and destination directories
from_dir = os.path.expanduser("~/Downloads")
to_dir = os.path.expanduser("~/Document_Files")

# Get the list of files in the source directory
list_of_files = os.listdir(from_dir)
print(list_of_files)

# Traverse through the list of files
for file_name in list_of_files:
    # Get the name and extension of each file
    name, ext = os.path.splitext(file_name)

    # Skip if extension is blank
    if not ext:
        continue

    # Check if extension is in the allowed list
    if ext.lower() in ['.txt', '.doc', '.docx', '.pdf']:
        # Create paths for source, destination directory, and destination file
        path1 = os.path.join(from_dir, file_name)
        path2 = os.path.join(to_dir, "Document_Files" + ext)
        path3 = os.path.join(path2, file_name)

        # Check if destination directory exists, if not create it
        if not os.path.exists(path2):
            os.makedirs(path2)

        # Move the file to the destination directory
        shutil.move(path1, path3)

        # Print a message to indicate file has been moved
        print(f"Moved {file_name} to {path3}")