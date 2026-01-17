import os
from pathlib import Path
import shutil

BASE_PATH = Path("./filesToOrganizase")


# Organizes the files individualy
def organize_files():
    try:
        count = 0

        for file in BASE_PATH.iterdir():
            if not file.is_file():
                continue

            ext = file.suffix.lower()

            if ext in (".txt", ".pdf", ".doc", ".docx"):
                dest = Path("./Folders/texts")
            elif ext in (".png", ".jpg", ".svg"):
                dest = Path("./Folders/images")
            elif ext in (".mp3", ".wav"):
                dest = Path("./Folders/audios")
            elif ext == ".mp4":
                dest = Path("./Folders/videos")
            elif ext in (".zip", ".rar", ".tar"):
                dest = Path("./Folders/compressed-files")
            else:
                continue

            dest.mkdir(parents=True, exist_ok=True)
            shutil.move(file, dest / file.name)
            count += 1

        print(f"{count} files have been moved")

    except Exception as e:
        print(f"An error has occurred: {e}")

#Show all the files inside the main folder ./filesToOrganize
def show_all_files():
    for file in BASE_PATH.iterdir():
        print(file)

# Organizes the files inside the main folder ./filesToOrganize
def move_file(fileToMove):
    try:
        fileToMove = BASE_PATH / fileToMove
        file_extension = fileToMove.suffix.lower()

        if not fileToMove.exists():
            print("this file does not exists")
            return
        
        if file_extension in (".txt", ".pdf", ".doc", ".docx"):
            shutil.move(fileToMove, "./Folders/texts")
        elif file_extension in (".png", ".jpg", ".svg"):
            shutil.move(fileToMove, "./Folders/images")
        elif file_extension in (".mp3", ".wav"):
            shutil.move(fileToMove, "./Folders/audios")
        elif file_extension == ".mp4":
            shutil.move(fileToMove, "./Folders/videos")
        elif file_extension in (".zip", ".rar", ".tar"):
            shutil.move(fileToMove, "./Folders/compressed-Files")

    except Exception as e:
        print(f"an error has ocurred {e}")

# THis functions gives to you in  formation about the file type you want to move
def file_info(file):
    file = BASE_PATH / file
    file_extension = file.suffix.lower()

    if file_extension in (".txt", ".pdf", ".doc", ".docx"):
        print("the file is a text, it will be moved to ./Folders/texts")
    elif file_extension in (".png", ".jpg", ".svg"):
        print("the file is an image, it will be moved to ./Folders/images")
    elif file_extension in (".mp3", ".wav"):
        print("the file is an audio, it will be moved to ./Folders/audios")
    elif file_extension == ".mp4":
        print("the file is a video, it will be moved to ./Folders/videos")
    elif file_extension in (".zip", ".rar", ".tar"):
        print("the file is a compressed file, it will be moved to ./Folders/compressed-Files")


# Main functionality

try:
    print("1-Move all files \n2-Move files individually \n3-File information")
    
    option = int(input())

    if option == 1:
        organize_files()
    elif option == 2:
        show_all_files()
        file = input("Add the file name you want to move: ")
        move_file(file)
    elif option == 3:
        show_all_files()
        file = input("Add the file name you want info: ")
        file_info(file)

except Exception:
    print("The option is invalid")
