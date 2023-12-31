# file sorter to sort your downloads folder based on file type

import os
import shutil

# folder names with their corresponding extension. if you want to add more, add here.
wow = {
    "documents": (
        ".pdf", ".xslx", ".docx", ".pptx", ".txt", ".odt", ".rtf", ".csv", ".md",
        ".tex", ".odp", ".ods", ".xml", ".html", ".epub", ".mobi", ".fb2"
    ),
    "video": (
        ".mkv", ".mp4", ".webm", ".mov", ".avi", ".m4v", ".m4a", ".hevc", ".flv", ".wmv",
        ".mpeg", ".mpg", ".vob", ".3gp", ".ts", ".ogv", ".m3u8"
    ),
    "audio": (
        ".mp3", ".wav", ".opus", ".aac", ".flac", ".m4a", ".wma", ".ogg", ".amr", ".mid",
        ".midi", ".ac3", ".aiff", ".au", ".ra"
    ),
    "photos": (
        ".jpeg", ".jpg", ".png", ".webp", ".heic", ".gif", ".ico", ".bmp", ".tiff", ".svg",
        ".eps", ".raw", ".cr2", ".nef", ".arw", ".orf", ".dng", ".sr2", ".rw2"
    ),
    "code": (
        ".html", ".css", ".py", ".js", ".php", ".rb", ".xml", ".json", ".pyw", ".c", ".sh",
        ".bat", ".cs", ".java", ".htm", ".pl", ".sql", ".cpp", ".h", ".m", ".swift", ".kt",
        ".vb", ".lua", ".scss", ".sass", ".less", ".ts"
    ),
    "archives": (
        ".zip", ".7z", ".rar", ".tar", ".gz", ".bz2", ".xz", ".iso", ".cab", ".arj", ".z",
        ".lzh", ".tgz", ".rpm", ".deb", ".dmg", ".img"
    ),
    "programs": (
        ".exe", ".msi", ".jar", ".apk", ".iso", ".msu", ".app", ".bat", ".cmd", ".sh", ".com",
        ".gadget", ".run", ".vb", ".vbs", ".ps1", ".psm1", ".psd1", ".reg", ".hta", ".appx",
        ".appxbundle", ".msp", ".msm", ".cpl", ".scr", ".pif", ".jar"
    ),
}

# change the string inside the brackets to your desired directory
os.chdir("/mnt/Storage/Downloads")

def folder_sort():
    """
    Logic to move folders into a folder named Folders. 
    """
    try:
        os.mkdir("Folders")
    except Exception as e:
        print("Folders already exists. Skipping")

    for i in os.listdir():
        if os.path.isdir(i) and i not in wow.keys() and i != "Folders":
            try:
                shutil.move(i, "Folders")
            except Exception as f:
                print(f)
                shutil.rmtree(i)
        else:
            pass

def file_sort(folder_name, file_extension, src_folder = ""):
    """
    Logic to sort files into their respective folders.

    Parameters:
        folder_name (dict key): Name of the folder
        file_extension (dict value): Extensions of that particular filetype
    """
    if src_folder == "": pass
    else: os.chdir(src_folder)
    
    try:
        os.mkdir(folder_name)
    except FileExistsError:
        print(f"{folder_name} already exists. Skipping....")

    for i in os.listdir():
        if i.endswith(file_extension):
            try:
                shutil.move(i, folder_name)
            except Exception:
                os.remove(i)

# start 
def main():
    folder_sort()
    for key, value in wow.items():
        file_sort(key, value)

if __name__ == "__main__":
    main()