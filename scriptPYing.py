import os
import shutil

def printDirAndFIles():

    for root, dirs, files in os.walk('../../..'):
        for dirname in dirs:
            print(os.path.join(root, dirname))

        for filename in files:
            print(os.path.join(root, filename))

def countDirsAndFIles():
    numberOfDirs = 0
    numberOfFIles = 0
    for root, dirs, files in os.walk('../../..'):
        for dirname in dirs:
            numberOfDirs += 1

        for filename in files:
            numberOfFIles += 1

    print "Number of directories: ", numberOfDirs
    print "Number of files: ", numberOfFIles



def deleteFile(fileNa):
    for root, dirs, files in os.walk('../../..'):
        for name in files:
            if(name == fileNa):
                print "Deleting file " + fileNa + "..."
                os.remove(os.path.join(root, fileNa))
                print("File was removed.")
                return

    print("File not found.")

def deleteDir(dirNa):
    for root, dirs, files in os.walk('../../..'):
        for dirname in dirs:
            if(dirname == dirNa):
                if os.listdir(os.path.join(root, dirNa)) == []:
                    print("Deleting empty directory " + dirNa + "...")
                    os.rmdir(os.path.join(root, dirNa))
                    print("Empty directory was deleted.")
                    return
                else:
                    print("Deleting directory " + dirNa + " and your content...")
                    shutil.rmtree(os.path.join(root, dirNa))
                    print("Directory was deleted.")
                    return

    print "Directory not found."

def spaceOccupied():
    size = 0
    for root, dirs, files in os.walk('../../..'):
        for fileName in files:
            size += os.path.getsize(os.path.join(root, fileName))

    if size >= 1073741824:
        print size / 1073741824, "GB"
    elif size >= 1048576:
        print size / 1048576, "MB"
    elif size >= 1024:
        print size / 1024, "KB"
    else:
        print size, "Bytes"

print "Welcome to PYing With Dir"
print
print "Remember that the script will work based on which directory the script is!"
print
print "Choose some option to use the script:"
print
print "Press 1 to list dirs and files\n"
print "Press 2 to count dirs and files\n"
print "Press 3 to delete some file\n"
print "Press 4 to delete some dir\n"
print "Press 5 to see how much memory is occupied in your compyter by files."
print

option = input("Choose an option: ")

if option == 1:
    print("Option chosen:  List dirs and files.")
    print
    print
    printDirAndFIles()
elif option == 2:
    print("Option chosen: Count dirs and files.")
    print
    print
    countDirsAndFIles()
elif option == 3:
    print("Option chosen: Delete some file.")
    print
    fileToDelete = raw_input("What's is your complete filename tha you want to delete: ")
    print
    print
    deleteFile(fileToDelete)
elif option == 4:
    print("Option chosen: Delete some directory.")
    print
    dirname = raw_input("What's is the directory you want to delete: ")
    print
    print
    deleteDir(dirname)
elif option == 5:
    print("Option chosen: See how much space is occupied.")
    print
    print
    spaceOccupied()
else:
    print("Wrong option.... Restart the script.")







