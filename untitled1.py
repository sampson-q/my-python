# -*- coding: utf-8 -*-
"""
Created on Sat May 30 10:58:36 2020

@author: Sampson Quarmy
"""

import string
status = ''
status1 = ''
consistArray = []
tempArray = []
temp1 = ''
temp = ''
message = input('Enter message: ')
messageLen = len(message)

# setting-up input syntax
messageSyntaxBox = ['-']
for digits in string.digits:
    messageSyntaxBox.append(digits)

# validating input [state0]
for codes in range(len(message)):
    if message[codes] in messageSyntaxBox:
        status = 'validationPassed'
    else:
        status = 'invalidCharacter'
# validating input [state1]
if message.count('-') != 0:
    if message[message.index('-')] == message[message.index('-') + 1]:
        status = 'syntaxErrorOn--'

# validating input [state2]
if status == 'invalidCharacter':
    print('Unknown char found in message. Message can only contain {}'.format(messageSyntaxBox))
    status = ''
elif status == 'syntaxErrorOn--':
    status = ''
    print('Incorrect combination of syntax. Check for consistent hyphens')

elif status == "validationPassed":
    status = ''
    try:
        for cdss in range(messageLen):
            if message[cdss] == message[cdss + 1]:
                consistArray.append(message[cdss])
                temp1 += message[cdss]
            else:
                if message[cdss] == message[cdss - 1]:
                    if message[cdss - 1] != message[-1]:
                        consistArray.append(message[cdss])
                    else:
                        status1 = 'additionPassed'
                    
    except IndexError as errorIgnored:
        status = errorIgnored
    status = ''
    counter = 0
    if consistArray != []:
        # get first two elements in consistArray
        while counter != 2:
            temp += consistArray[counter]
            counter += 1
        # removing first consistArray element if first two elements of temp and consistArray don't match
        if message[0:2] != temp:
            consistArray.insert(-1, consistArray[0])
            consistArray.pop(0)
        
        if status1 == 'additionPassed':
            consistArray.append(consistArray[-1])
        
print(consistArray)