"""
BELOW TO MAKE THE MATRIX:
    MAKE MASTER EMPTY LIST
    MAKE FOR LOOP FOR 5 INPUTS
    SPLIT FUNC FOR 5 INPUT

FIND OPTIMAL POSITION:
    OPTIMAL POSITION = master[2][2]

    1. FIND POSITION OF 1
    2. CALCULATE TRAVERSAL [USED MANHATTAN DISTANCE FORMULA]
"""

master = []

for i in range(5):
    x = input()
    if x == " ":
        continue
    master.append(x.split())

for i in master:
    for j in i:
        if j == "1":
            y = master.index(i),i.index("1")

opt = (abs(int(y[0]) - 2)) + (abs(int(y[1]) - 2))
print(opt)
