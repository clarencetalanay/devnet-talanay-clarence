"""
Module 2 — Activity: File Sorting with os and shutil
Student: [Clarence Nathan Lee D. Talanay]
Date: [9/27/2026]

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
[A customized file organizer in python that scans a 
designated directory, extracts file extensions,
and automatically routes files into categorized subfolders. 
It also includes safeguards to handle name collisions and protect the script 
file itself from being moved.]


============================================
KEY VOCABULARY
============================================
- os module: built-in library to interact with the operating system
- shutil module: high-level library used to move and copy files
- file path: the unique location of a file or folder on the computer
- directory: a folder used to organize files
(add more as needed)

============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

#folder names to file extensions
FILE_TYPES = {
    "Visual_Media": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp"],
    "Docs": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Sound": [".mp3", ".wav", ".flac", ".m4a"],
    "Clips": [".mp4", ".mkv", ".mov", ".avi"],
    "Zips": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Scripts": [".py", ".html", ".css", ".js", ".json", ".cpp"]
}

def organize_directory(path_input="."):
    base_dir = os.path.abspath(path_input)

    if not os.path.isdir(base_dir):
        print(f"[X] Invalid directory path: {base_dir}")
        return

    tally = 0
    
    # Iterate through items in the target path
    for entry in os.listdir(base_dir):
        source_path = os.path.join(base_dir, entry)

        # Skip directories and safeguard against moving the script file itself
        if os.path.isdir(source_path) or os.path.abspath(source_path) == os.path.abspath(__file__):
            continue

        name_part, file_suffix = os.path.splitext(entry)
        file_suffix = file_suffix.lower()

        # Ignore files without extensions
        if not file_suffix:
            continue

        # Match extension to group, default to 'Misc'
        assigned_folder = "Misc"
        for group_name, suffixes in FILE_TYPES.items():
            if file_suffix in suffixes:
                assigned_folder = group_name
                break

        target_dir_path = os.path.join(base_dir, assigned_folder)
        os.makedirs(target_dir_path, exist_ok=True)

        destination_path = os.path.join(target_dir_path, entry)

        # Prevent overwriting by appending a unique tag if a file name clashes
        if os.path.exists(destination_path):
            destination_path = os.path.join(target_dir_path, f"{name_part}_bak{file_suffix}")

        # Execute the move
        shutil.move(source_path, destination_path)
        print(f"-> Relocated '{entry}' into '{assigned_folder}/'")
        tally += 1

    print(f"\nDone! Successfully cleaned up {tally} file(s).")


if __name__ == "__main__":
    user_path = input("Path to clean (leave blank for current folder): ").strip()
    organize_directory(user_path if user_path else ".")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[The script trying to move itself or crashing when trying to move 
files into a folder that doesn't exist yet.]


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[Similar to automating a cleanup in a messy folder.]
"""
