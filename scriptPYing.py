import os
import shutil

def printDirAndFIles():

    for root, dirs, files in os.walk('.'):
        for dirname in dirs:
            print(os.path.join(root, dirname))

        for filename in files:
            print(os.path.join(root, filename))

def countDirsAndFIles():
    numberOfDirs = 0
    numberOfFIles = 0
    for root, dirs, files in os.walk('.'):
        for dirname in dirs:
            numberOfDirs += 1

        for filename in files:
            numberOfFIles += 1

    print "Number of directories: ", numberOfDirs
    print "Number of files: ", numberOfFIles



def deleteFIle(file):
    found = 0
    for root, dirs, files in os.walk('.'):
        for name in files:
            if(name == file):
                found = 1

    if(found == 1):
        print("Deletando ", file, ".....")
        os.remove(file)
        print("Deletado")
    else:
        print("Nao achamos o arquivo requerido.")

def deleteDir(dir):
    found = 0
    for root, dirs, files in os.walk('.'):
        for dirname in dirs:
            if(dirname == dir):
                found = 1

    if(found == 1):
        if os.listdir(dir) == []:
            print("Deletando diretorio vazio " + dir + "...")
            os.rmdir(dir)
            print("diretorio vazio deletado.")
        else:
            print("Deletando diretorio " + dir + " e seu conteudo...")
            shutil.rmtree(dir)
            print("diretorio deletado.")
    else:
        print("Nao achamos o diretorio requerido.")

print "Welcome to PYing With Dir"
print
print "Remember that the script will work based on which directorie the script is!"
print
print "Choose some option to use the script:"
print
print "Press 1 to list dirs and files\n"
print "Press 2 to count dirs and files\n"
print "Press 3 to delete some file\n"
print "Press 4 to delete some dir\n"
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
    fileToDelete = raw_input("What's is our complete filename tha you want to delete: ")
    print
    print
    deleteFIle(fileToDelete)
elif option == 4:
    print("Option chosen: Delete some directorie.")
    print
    dirname = raw_input("What's is the directorie you want to delete: ")
    print
    print
    deleteDir(dirname)
else:
    print("Wrong option.... Restart the script.")







