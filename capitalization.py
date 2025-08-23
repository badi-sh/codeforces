"""
CAPITALIZE THE FIRST LETTER OF A STRING. KEEP REST SAME.

MY CODE:
x = input()

if x[0].islower() == True:
    print(x[0].upper()+x[1:])
else:
    print(x)

PP CODE (OPTIMIZED):
print(x[0].upper()+x[1:])
"""

x = input()

if x[0].islower() == True:
    print(x[0].upper()+x[1:])
else:
    print(x)
