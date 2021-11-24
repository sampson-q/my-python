# -*- coding: utf-8 -*-
"""
Created on Sat May 30 07:06:57 2020

@author: Sampson Quarmy
"""

codeArray = []
code = []
spacePossDouble = []
spacePossSingle = []
seivedArray = []
seivedString = ''
checker = ''
status = ''
tempCodes = ''
speCodeIndex = 0

codes = input('Enter codes: ')

for elements in codes:
    code.append(elements)

if code[0] == '-':
    print('Error. First character cannot be = to "{}"'.format(code[0]))
elif code[-1] == '-':
    print('Error. Last character cannot be = to "{}"'.format(code[-1]))
else:
    for codeCounter in range(len(code)):
        if code[codeCounter] == '-':
            if code[codeCounter] == code[codeCounter + 1]:
                checker += code[codeCounter]
                index = code.index(code[codeCounter])
                spacePossDouble.append(index)
                if code.count('-') != 0:
                    code.pop(index)
                
print(spacePossDouble, end='')
print()
print(spacePossSingle, end='')

"""    if checker.count('-') > 1:
        if checker.count('-') % 2 != 0:
            print('Error. Three consistent "-" in code')
        else:
            status = 'continue'
    else:
        status = 'continue'
"""

"""
    else:
        if codes == '-':
            print(codes, end='.')

"""
"""    
for counter in range(len(codeArray)):
    for positionCounter in range(len(codeArray) - 1):
        if codeArray[positionCounter] == codeArray[positionCounter + 1]:
             seivedArray.append(codeArray[positionCounter + 1])
        else:
            seivedArray.append(codeArray[positionCounter])
            seivedArray.append('-')
    seivedArray.append(codeArray[-1])
    break

for seivedCodes in seivedArray:
    seivedString += seivedCodes
    
print(seivedString) """