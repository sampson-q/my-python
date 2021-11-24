# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 21:35:30 2021

@author: Hash
"""


U = [4, 5, 3, 12, 65, 77, 30, 454]
sortedList = []
temp = []

for i in range(0, len(U)):
    for e in range(0, len(U) - 1):
        if U[i] > U[e]:
            tu = U[e]
            U[i] = U[e]
            tu = U[e]
    sortedList.append(U[i])

print(sortedList)