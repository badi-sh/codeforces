"""
If len(string) > 10
Keep first and last letter and put no. of letters in between first and last

end -> Declares what should be at the end of print statement

localization
12
TRUE
i = 0 to 11

1st Iteration:
i = 0
Cond1: TRUE or FALSE -> TRUE
    l
Cond2: TRUE
    10

2nd Iteration:
i = 1
Cond1: FALSE

UNOPTIMIZED [MY LOGIC]:
x = int(input())

for j in range(x):
    string = input()
    length = len(string)

    if length > 10:
        for i in range(length):
            if i == 0 or i == length-1:
                print(string[i],end="")
                if i != length-1:
                    print(length-2,end="")
        print()
    else:
        print(string)

OPTIMIZED [PP VERSION]:
x = int(input())
for j in range(x):
    y = input()
    if len(y) > 10:
        print(y[0]+str(len(y)-2)+y[-1])
    else:
        print(y)
"""
x = int(input())
for j in range(x):
    y = input()
    if len(y) > 10:
        print(y[0]+str(len(y)-2)+y[-1])
    else:
        print(y)



