import random
firstNameHandler = open("First names.txt","r")
firstNames = firstNameHandler.readlines()
firstNamesNum = len(firstNames)

middleNameHandler = open("Middle names.txt","r")
middleNames = middleNameHandler.readlines()
middleNamesNum = len(middleNames)

lastNameHandler = open("Last names.txt","r")
lastNames = lastNameHandler.readlines()
lastNamesNum = len(lastNames)

print(firstNames[random.randint(0,firstNamesNum-1)].rstrip(), end = ' ')
if random.randint(0,1):
    print(middleNames[random.randint(0,middleNamesNum-1)].rstrip(), end = ' ')
if random.randint(0,3):
    print(lastNames[random.randint(0,lastNamesNum-1)].rstrip(), end = ' ')


