"""
TAKE TWO NUMBERS AS INPUT
n is actual number
k is no. of times to perform operations.

If last digit of n == 0, Divide by 10
If last digit of n != 0, Subtract by 1

Print value derived after k no. of subtractions on n.

ADDITIONAL INFO:
Modulo is used as remainder of any num divided by 10 would be its last digit.
EX: 512 % 10 -> STEP 1: 10 * 51 = 510
                STEP 2: 512 - 510 = 2
                STEP 3: REMAINDER = 2 i.e. last digit

"""

x = input().split()
n = int(x[0])
k = int(x[1])

for i in range(k):
    if n % 10 != 0:
        n -= 1
    else:
        n //= 10
    
print(n)