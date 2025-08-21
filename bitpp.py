"""
NO NOTES. GG EZ.
"""

x = int(input())
num = 0

for i in range(x):
    y = input()
    if y == "++X" or y == "X++":
        num += 1
    if y == "--X" or y == "X--":
        num -= 1
print(num)