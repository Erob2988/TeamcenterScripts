"""
Script to read input file and create a lst file I can user to update all 
users license level.
"""

inputFile = open("C:/Users/pbxg9v/Documents/Make_User_011320",'r')
outputFile = open("C:/Users/pbxg9v/Documents/User_Update_011320", 'w')
#user id starts at charater 48

for line in inputFile:
    password = line.find("-password=")
    #print("\""+ line[48:password-1] + "\"")
    outputFile.write("|" + line[47:password-1] + "||||licenselevel|consumer|update\n")

inputFile.close()
outputFile.close()