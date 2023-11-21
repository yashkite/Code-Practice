### File Sorter Script

The provided script is a Python program designed to organize the contents of a specified directory, such as a Downloads folder, by moving files into folders based on their types. The script categorizes files into different folders depending on their extensions (file types).

### Usage

1. **Folder Sorting**

    - The script first creates a folder named "Folders" if it doesn't already exist.
    - It then moves all non-special folders (not listed in the `wow` dictionary) into the "Folders" directory.

2. **File Sorting**

    - For each category in the `wow` dictionary, the script creates a folder with the category name.
    - Files with extensions corresponding to each category are then moved into their respective folders.

### Script Structure

```python
import os
import shutil

# Dictionary of folder names and their corresponding file extensions
wow = {
    "documents": (".pdf", ".xslx", ".docx", ".pptx", ".txt", ".odt", ".rtf", ".csv", ".md", ...),
    "video": (".mkv", ".mp4", ".webm", ".mov", ...),
    # ... (other categories)
}

# Change the directory to your desired directory
os.chdir("/mnt/Storage/Downloads")

# Function to move non-special folders into a folder named "Folders"
def folder_sort():
    # ...

# Function to sort files into their respective folders
def file_sort(folder_name, file_extension, src_folder=""):
    # ...

# Main function to execute folder and file sorting
def main():
    # ...

if __name__ == "__main__":
    main()
```

### Considerations

1. **Directory Path**: The script is configured to work in the specified directory (`"/mnt/Storage/Downloads"`). You can change this path to the directory you want to organize.

2. **Special Folders**: Folders listed in the `wow` dictionary are considered special folders, and files with matching extensions are moved into these folders. Other folders are moved into a folder named "Folders."

3. **Error Handling**: The script contains minimal error handling. You might want to enhance it based on potential issues that may arise during folder and file operations.

4. **Extensions**: You can customize the `wow` dictionary to include additional file types or create new categories.

### Example Usage

```python
python file_sorter.py
```

This script can be run in the command line or integrated into other programs as needed. It provides a convenient way to organize files based on their types.