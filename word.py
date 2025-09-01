"""
CONVERT MIX CASE WORDS TO UPPER OR LOWER CASE
IF NO. OF LETTER WITH UPPERCASE IS MORE, PRINT UPPERCASE
ELSE PRINT LOWERCASE
IF NO. OF UPPER == NO. OF LOWER, PRINT LOWERCASE

CASE 1:
IN: HoUse
OUT: house
"""
x = input()
high = 0
low = 0

for i in x:
    if i.isupper() == True:
        high += 1
    else:
        low += 1

if high > low:
    print(x.upper())
else:
    print(x.lower())