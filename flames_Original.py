# -*- coding: utf-8 -*-
"""
Created on Sun May 31 07:18:33 2020

@author: Sampson Quarmy
"""

# initializing boy's name list
boyList = []
# initializing girl's name list
girlList = []
# initializing sorted names' list
extList = []
# initializing the counter of the algorithm
counter = 0
# preparing the flames
flames = ['Friends!', 'Lovers!', 'Arranging for Marriage!', 'Married Couples!', 'Enemies!', 'Secret Lovers!']

# controlling user-input such that it != null
while True:
    # accepting user input (boy's name)
    boyName = input('Boy\'s Name: ')
    # accepting user input (girl's name)
    girlName = input('Girl\'s Name: ')
    # conditioning the program to reject empty names
    if boyName == '' or girlName == '':
        # relaying an error message if any name comes unprovided
        print('No name can be empty. Check the names and try again \a')
    # conditioning the program to break the loop if all names are provided
    else:
        # breaking the loop
        break

# casing boy's name to lower
for boyLetters in boyName:
    boyList.append(boyLetters.lower())

# casing girl's name to lower
for girlLetters in girlName:
    girlList.append(girlLetters.lower())    

# spacing out inputs and outputs
print()

# conditioning program to reject inputs if both names are ==
if boyName != girlName:
    # conditioning the program to compare the length of both names
    if len(boyName) > len(girlName):
        # initializing 'status' to 'useBoyNameLen' if boy's name length exceed the girl's
        status = 'useBoyNameLen'
        # initializing counter of the operation to the number of letters in boy's name
        counter = len(boyName)   
    # else statement of comparing the number of letters in both names
    else:
        # setting the variable 'status' to 'useGirlNameLen' if girl's name letters exceed the boy's
        status = 'useGirlNameLen'       
        # setting the counter of the operation to the number of letter in the girl's name
        counter = len(girlName)   
    # catching and throwing index error
    try:
        # defining the counter of the operation
        while counter != 0:
            # conditioning the program to check its status
            if status == 'useGirlNameLen':
                # baiting the program for InS

                try:
                    # loop for comparing and eliminating like terms in both names
                    for girlCounter in range(len(girlList)):
                        for boyCounter in range(len(boyList)):
                            if boyList[boyCounter] == girlList[girlCounter]:
                                boyList.remove(boyList[boyCounter])
                                girlList.remove(girlList[girlCounter])
                # handling IndexError
                except IndexError as e:
                    error = e
            # else part of the condition
            else:
                # catching IndexError
                try:
                    # comparing and eliminating like terms in both names
                    for boyCounter in range(len(boyList)):
                        for girlCounter in range(len(girlList)):
                            if boyList[boyCounter] == girlList[girlCounter]:
                                boyList.remove(boyList[boyCounter])
                                girlList.remove(girlList[girlCounter])
                # handling IndexError
                except IndexError:
                    pass
            # decrement of the counter variable
            counter -= 1
    # handling IndexError
    except IndexError:
        pass
    # merging sorted names into extList
    extList.extend(boyList)
    extList.extend(girlList)
    # fetching and displaying the result of the operation to the user
    print('{} and {} are {} \a'.format(boyName, girlName, flames[(len(extList) % len(flames)) - 1]))
# else statement for == names
else:
    print('Both names cannot be the same. Check the names and try again')