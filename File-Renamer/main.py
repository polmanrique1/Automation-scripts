import os
from pathlib import Path


# THis function list all the files in the folder named files
def listFiles():

    if (not os.path.exists("./files")):
        return print("the directory ./files does not exist")

    for i in os.listdir("./files"):
        print(i);

# This folder changes the name of the file you passed to it
def changeFileName(oldFile, newFile):

    base_path = Path("./files")
    old_path = base_path / oldFile
    new_path = base_path / newFile
    
    if (not os.path.exists(old_path)):
        return print("the file you want to change dosent exist")
    
    if (os.path.exists(new_path)):
        return print("the file name alredy exists")
    
    os.rename(old_path, new_path)

    return print("file name changed succesfully")


# This funciton changes all the names of the files in the folder file
def changeAllFileNames(fileName):

    base_path = Path("./files")

    count = 0;
    try:
        for file  in base_path.iterdir():
            if file.is_file():
                file_extension = file.suffix
                new_name = f"{fileName}_{count}{file.suffix}"
                file.rename(base_path / new_name)
                count+=1

        return print(f"All the file names has been changed successfuly \n {count} files have been changed") 
    except Exception as e:
        return print(f"An error has ocurred {str(e)}")

try:

    print("##### Files ##### \n")

    listFiles()

    print("\n")

    print("1- Change a file name \n 2-change all file names")

    option = input()

    if not option.isdigit():
        print("Invalid option, option must be a number beteen 1 and 2")
    
    option = int(option)

    if option == 1:

        oldFile = input("Write the file name you want to change: ")
        newFile = input("write the new file name:  ")

        changeFileName(oldFile, newFile)
    elif option == 2:
        fileName = input("File name: ")
        
        changeAllFileNames(fileName)


except Exception as e:
    print(f"something worng has ocurred during the proces  {str(e)}")