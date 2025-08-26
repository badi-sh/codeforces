"""
W = NO. OF BANANA
K = BANANA PRICE
N = CURRENT DOLLARS
"""

x = input().split()
k = int(x[0])
n = int(x[1])
w = int(x[2])

tot = 0

for i in range(1, w+1):
    price = i * k
    tot += price

if tot<=n:
    print(0)
else:
    borr = tot - n
    print(borr)
