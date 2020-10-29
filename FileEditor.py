# Safin Stefanos
# 10/29/2020
# File Editor
# Random Variable Names
# a is for the answer of if you want to delete the file
# b is for the answer of do you want to add anything to your file (append)
# c is for the answer of do you want to write anything else in your file (add warning here)
import os
import time
import sys
#Name File
FileName = input("\nWhat do you want your file name to be? You do not need to add a file extension.\n")
FileName = FileName + ".txt"
#Create file
File = open(FileName, "w")
# What goes inside the file
StuffInside = input("""What would you like to be in this file? If you already have a file
with this name everything inside of it will be written over.\n""")
File.write(StuffInside)
File.close()
x = 1
while x == 1:
    print("***************************************************")
    print("*                   File Editor                   *")
    print("*      Instructions: Here you can create your     *")
    print("*     own file. You can add to it, write over     *")
    print("*            the file, delete the file,           *")
    print("*        and view what is inside the file.        *")
    print("*                                                 *")
    print("*  Choose an option                               *")
    print("*  1. Rewrite File                                *")
    print("*  2. Add to file                                 *")
    print("*  3. View File                                   *")
    print("*  4. Rename File                                 *")
    print("*  5. Delete File                                 *")
    print("*  6. Exit Editor                                 *")
    print("*  7. Restart                                     *")
    print("***************************************************")
    answer = input("Insert a number to use the editor.\n")
#Rewrite
    if answer == "1":
        rewrite = input("Are you sure you want to rewrite over your file. This will delete all previous data.\n")
        if rewrite == "yes" or rewrite == "y" or rewrite == "Yes" or rewrite == "YES" or rewrite == "Y":
            File=open(FileName, "w")
            abcd = input("What would you like to write?\n")
            File.write(abcd)
            File.close()
            print("You will be returned to the menu in 2 seconds.\n\n")
            time.sleep(2)
#Add to file
    if answer == "2":
        File=open(FileName, "a")
        change = input("What would you like to add?\n")
        File.write(change + "\n")
        File.close()
        print("You will be returned to the main menu in 2 seconds.\n\n")
        time.sleep(2)
#View file
    if answer == "3":
        File=open(FileName, "r")
        print(File.read())
        File.close()
        print("You will be returned to the menu in 2 seconds.\n\n")
        time.sleep(2)
#Rename File
    if answer == "4":
#FileName is default name without txt
#FileNamePath is the path of FileName
#FilePath is the path without the FileName with txt in it
#FileNamePath is the path with the FileName with txt in it
#NewFileName is what the user wants to change the File Name to
        FileNamePath = os.path.join(os.path.dirname(__file__), FileName)
        FilePath = FileNamePath.replace(FileName,"")
        NewFileName = input("What do you want your file to be called? Once again no file extension required.\n")
        FileName = NewFileName + ".txt"
        NewFileName = FilePath + NewFileName + ".txt"
        os.rename(FileNamePath, NewFileName)
        print("You will be returned to the menu in 2 seconds.\n\n")
        time.sleep(2)
#Delete File
    if answer == "5":
        a = input("Are you sure you want to delete " + FileName + "?")
        if a == "yes" or a == "y" or a == "Yes" or a == "YES" or a == "Y":
            os.remove(FileName)
            print("The editor will close in 2 seconds.\n\n")
            time.sleep(2)
#Exit editor
    if answer == "6":
        exit()
#Restart
    if answer == "7":
        os.execl(sys.executable, sys.executable, *sys.argv)
