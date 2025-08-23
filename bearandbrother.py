"""
TWO VAR A AND B.
A IS TRIPLED EVERY ITERATION.
B IS DOUBLED EVERY ITERATION.

CALCULATE NO. OF ITERATIONS IT WILL TAKE FOR A TO BE BIGGER THAN B.

INPUT: 4, 9
YEAR 1:
4 * 3 = 12
9 * 2 = 18

YEAR 2:
12 * 3 = 36
18 * 2 = 36

YEAR 3:
36 * 3 = 108
36 * 2 = 72

108 = 4 * 3 * 3 * 3 == 4 * 3^3
72 = 9 * 2 * 2 * 2 == 9 * 2^3
"""
x = input().split()
n = 1
count = 0

a = int(x[0]) * 3 ** n
b = int(x[1]) * 2 ** n

while(a<=b):
    n+=1
    a = int(x[0]) * 3 ** n
    b = int(x[1]) * 2 ** n

print(n)
