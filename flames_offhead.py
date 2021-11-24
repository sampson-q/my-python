# -*- coding: utf-8 -*-
"""
Created on Sun May 31 07:18:33 2020

@author: Sampson Quarmy
"""

boyList = []
girlLit = []
likeTerms = []
unlikeTerms = []
boyName = input('Enter Name of Boy: ')
girlName = input('Enter Name of Girl: ')


for boyLetters in boyName:
    boyList.append(boyLetters)

for girlLetters in girlName:
    girlList.append(girlLetters)

# check for lenght of both names

status = ''

if len(boyName) > len(girlName):
    status == 'boy'
else:
    status == 'girl'

if status == 'boy':
    for i in range(0, len(status)):
        try:
            for boyters in boyName:
                for girlters in girlName:
                    if boyName.index(boyName[boyters]) == girlName.index(girlName[girlters]):
                        boyList.remove(boyters)
                        girlList.remove(girlters)
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            

try:
    

for alphabets in boyName:
    for alphabet in girlName:
        if boyName[alphabets] == girlName[alphaber]:
            unlikeTerms.extend(boyName[alphabets])