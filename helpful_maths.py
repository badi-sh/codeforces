"""
PUT NUMBER IN ASCENDING ORDER
INPUT:
3+1+2
OUTPUT:
1+2+3
"""

x = input().split('+')
y = sorted(x)

for i in range(len(y)):
    if i == len(y)-1:
        print(y[i])
    else:
        print(y[i], end="+")
    
