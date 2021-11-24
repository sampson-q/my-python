# -*- coding: utf-8 -*-
"""
Created on Sun May 16 18:25:46 2021

@author: Hash
"""


marks = [10, 20, 30, 40, 50, 60]
frequency = [5, 4, 2, 7, 9, 3]

sigmafx = 0
sigmafx = float(sigmafx)

sigmaf = 0
sigmaf = float(sigmaf)

for i in range(0, len(marks)):
    sigmafx += (marks[i] * frequency[i])
    sigmaf += frequency[i]
    
mean = sigmafx / sigmaf

frequency2 = frequency
frequency.sort()
largestNumber = frequency2[-1]

median = 0
median1 = 0

if len(marks) % 2 != 0:
    median = marks[len(marks) / 2]
else:
    for i in frequency:
        median1 += 1
        if median1 >= sigmaf / 2:
            for y in range(len(marks)):
                if frequency[y] == i:
                    median = marks[y]

print('\nFREQUENCY DISTRIBUTION TABLE')
print("-------------------------------------------------")
print("|   Marks (x)   |   Frequency (f)   |     fx    |")
print("-------------------------------------------------")

for i in range(0, len(marks)):
    print("|       " + f"{marks[i]}" + "\t|       " + 
          f'{frequency[i]}\t    ' + "|\t" + 
          f'{marks[i] * frequency[i]}' + "   \t|")

print("-------------------------------------------------")
print("|     Totals \t|      " + f'{sigmaf}' + "\t    |  " + f'{sigmafx}' + "\t|")
print("-------------------------------------------------")

modes = []

for i in frequency:
    if i == largestNumber:
        modes.append(i)

for i in modes:
    print('\nMode(s): {},'.format(i))

print('Mean: {}'.format(mean))
print('Median: {}'.format(median))

print('\nHISTOGRAM')
print('\n\t   y\n\t   ^', end="")

for i in range(largestNumber, 0, -1):
    if i > 9:
        print("\n\t" + f'{i}' + " |")
    else:
        print("\n\t " + f'{i}' + " |")
    
    for j in range(0, len(marks)):
        if frequency[j] >= i:
            print("   x-x", end='---->')
        else:
            print("      ", end="---->")
    
print("\n\t   ------------------------------------------> x\n\t   0")