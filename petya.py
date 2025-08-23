"""
Show that value of letter is equal to number without ascii

CONDITION 1: abe ace
i = 1
x = a, y = a
OUT: 0

i = 2
x = b, y = c
OUT: -1

i = 3
x = e, y = e
OUT: 0
"""

x = input().lower()
y = input().lower()

for i in range(len(x)):
    if x[i] == y[i] and i == len(x)-1:
        print(0)
    if x[i] > y[i]:
        print(1)
        break
    if x[i] < y[i]:
        print(-1)
        break





    
    



