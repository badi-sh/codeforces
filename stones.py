"""
WRITE A CODE THAT TAKES AND INTEGER WITH STRING WITH RGB STONES
CALCULATE HOW MANY STORNES NEED TO BE TAKEN TO HAVE DIFFERENT STONES SET.

INPUT:
3
RRG

i = 0
y[0] = R
y[0 + 1] = R
UPDATED y = RG

"""
x = int(input())
y = input()
i = 0
count = 0

while(i<x-1):
    if y[i] == y[i+1]:
        count+=1
    i += 1
print(count)


        
