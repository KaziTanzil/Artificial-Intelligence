# -*- coding: utf-8 -*-
"""Queen Attack Detection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eFKEyXjeJNRCiFjsw7q4Ha7EgTWs043U

# N Queen Attack Detection

![image.png](data:image/png;base64,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)
"""

def drawBoard(P):
  n = len(P)
  for i in range(1,n+1):
    print("|", end="")
    for j in range(1,n+1):
      if (i,j) in P:
        ind = str(1+ P.index((i,j)))
        print(" "+ind+" |", end= "")
      else:
        print(" * |", end= "")
    print()

import random
def generate_positions(n):
    numbers = list(range(n**2))
    random.shuffle(numbers)
    print(numbers)
    P = []
    for i in range(n):
        row = numbers[i]//n + 1
        col = numbers[i]%n + 1
        P.append((row,col))
    return P

pos = generate_positions(4)
print(pos)
drawBoard(pos)

# row attack
def rowAttacK(P):
  n = len(P)
  count = 0
  for i in range(n):
    for j in range(i+1,n):
      if P[i][0] == P[j][0]:
        print('row attack:', end = " " )
        print(i+1,P[i], end = ", ")
        print(j+1,P[j])
        count = count + 1
  return count

rowAttacK(pos)

abs(-2)

#column attack
def columnAttacK(P):
  n = len(P)
  count = 0
  for i in range(n):
    for j in range(i+1,n):
      if P[i][1] == P[j][1]:
        print('column attack:', end = " " )
        print(i+1,P[i], end = ", ")
        print(j+1,P[j])
        count = count + 1
  return count

columnAttacK(pos)

# diagonal atack
def DiagonalAttacK(P):
  n = len(P)
  count = 0
  for i in range(n):
    for j in range(i+1,n):
      if abs(P[i][0]-P[j][0])==abs(P[i][1]-P[j][1]):
        print('Diagonal attack:', end = " " )
        print(i+1,P[i], end = ", ")
        print(j+1,P[j])
        count = count + 1
  return count

DiagonalAttacK(pos)

# implement a method to print a state is valid or not
def isValid(P):




    if rowAttacK(P) > 0:

        return False
    elif columnAttacK(P) > 0:

        return False
    elif DiagonalAttacK(P) > 0:

        return False


    return True
    print(pos)
drawBoard(pos)

if isValid(pos):
        print("valid")
else:
        print("invalid")

from collections import Counter
# call isValid untill you get valid solution
import random
valid=False
Count = 0
while not valid:
    pos=generate_positions(4)
    Count = Count + 1
    if isValid(pos):

        valid=True
print(pos)
drawBoard(pos)
print('Number of Count',Count)