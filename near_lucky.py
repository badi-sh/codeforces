"""
CALCULATE NUMBER OF 4'S AND 7'S IN A NUMBER
IF THE TOTAL VALUE OF 4'S AND 7'S IS A LUCKY NUMBER, 
    NUMBER IS NEAR LUCKY
ELSE 
    NUMBER NOT NEAR LUCKY
"""

x = input()
luck = 0

for i in x:
    if i == "4" or i == "7":
        luck += 1

if "7" in str(luck) or "4" in str(luck):
    print("YES")
else:
    print("NO")