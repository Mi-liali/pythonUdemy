# -*- coding: utf-8 -*-

# Part_1

a = 9
b = 17
c = 5

bull = None

bull = a > b
print(bull)

bull = a == (b - c)
print(bull)

bull = b == (a + c)
print(bull)

bull = c <= (a + b)
print(bull)

bull = b > a > c
print(bull)

bull = b < a or b < c
print(bull)

# Part_2

bull_2 = None
bull = bull_2 is True
print(bull)
bull = bull_2 is False
print(bull)
bull = bull_2 is None
print(bull)

# Part_3

# A! and (C or A) and (B or C!)

A = 1
nA = 0
B = 0
C = 1
nC = 0
bull = (nA and (C or A) and (B or nC))

print(bull)
