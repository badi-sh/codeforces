"""
Calculate the number of squares that can fit in n*m area of rectangle
"""
import math

x = input().split()
n = int(x[0])
m = int(x[1])
a = int(x[2])

print(math.ceil(n/a) * math.ceil(m/a))




# n = 1
# m = 1
# a = 1
# c = 0
# k = 0

# while n > 0:
#     n -= a
#     c += 1

# while m > 0:
#     m -= a
#     k += 1


# print(c*k)

