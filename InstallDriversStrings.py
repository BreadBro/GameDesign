strDrivers="""Here are the instructions to install Drivers
1. After the download is completed go to where you saved the folder.
(By default everything you download from the Internet is saved to the Downloads folder)
2. Right click on the folder and choose ''Extract All'' and then choose ''Extract'' again.
3. Once all the contents have been extracted you may delete/disregard the folder with the zip icon.
4. Next, open and Run the SETUP file. (In most cases it is a setup.exe file OR one listed below:
*setup application
*Asussetup
*pnpinstal64
*pnputil
*Igxpin
5. Please choose to 'repair' or 'update' the existing installation (driver) IF any one of those options do appear during the set up.
"""
subStr="Drivers"
print(strDrivers.count(subStr))
print(strDrivers)
print(len(strDrivers))
strDrivers=(strDrivers.replace("Extract", "EXTRACT"))
strDrivers=(strDrivers.replace("Setup", "SETUP"))
indexNum=strDrivers.find("4")
print(indexNum)
indexNum=strDrivers.find("1.")
print(strDrivers[indexNum: indexNum+156], "\n")
indexNum=strDrivers.find("2.")
print(strDrivers[indexNum: indexNum+90], "\n")
indexNum=strDrivers.find("3.")
print(strDrivers[indexNum: indexNum+99], "\n")
indexNum=strDrivers.find("4.")
print(strDrivers[indexNum: indexNum+156], "\n")
indexNum=strDrivers.find("5.")
print(strDrivers[indexNum: indexNum+132], "\n")
#print(indexNum)
#print(len(indexNum))
# Find how many times the word Drivers is used
# How long in your Strint
# Replace Extract with EXTRACT
# Replace setup or Setup with SETUP
# Find  ‘4’
# Find the 1 and print until you find the end of the statement
# Find the 2 and print until you find the end of the statement
# Find the 3 and print until you find the end of the statement
# Find the 4 and print until you find the end of the statement
# Find the 5 and print until you find the end of the statement
