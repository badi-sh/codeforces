"""
TWO INPUTS
INPUT 1 IS NUMBER OF GAMES
INPUT 2 IS STRING OF A AND D

COUNT NUMBER OF A'S AND D'S IN THE STRING
IF NO. OF A > NO. OF D
PRINT ANTON

IF NO. OF A < NO. OF D
PRINT DANIK

IF BOTH SAME
PRINT FRIENDSHIP
"""

x = int(input())
y = input()
a = 0
d = 0

for i in y:
    if i == "A":
        a += 1
    else:
        d += 1

if a > d:
    print("Anton")
elif a < d:
    print("Danik")
else:
    print("Friendship")