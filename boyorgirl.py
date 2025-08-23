"""
IDENTIFY UNIQUE OCCURENCES OF CHAR IN PYTHON.
IF ODD THEN MALE
IF EVEN THEN FEMALE

LEARNED ABOUT SET:
SET IS IMMUTABLE, RANDOM, UNIQUE
"""

red = input()
# x = len(set(red))

# if x % 2 == 0:
#     print("CHAT WITH HER!")
# else:
#     print("IGNORE HIM!")

x = []
for i in red:
    if i not in x:
        x.append(i)

if len(x) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
