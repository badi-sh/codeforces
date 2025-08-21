"""
n = NO. OF PARTICIPANTS
k = POSITION OF PARTICIPANT

Find how many participants are allowed to go to next round
Win Condition: Score of player >= Score of K

n k
for i in range(n) -> Loop for the number of players
Add the Scores to a list

MY CODE:
nk = input().split()
count = 0

num = input()
x = num.split()
for j in x:
    if int(j) > 0:
        if int(j) >= int(x[int(nk[1])-1]):
            count += 1
print(count)

OPTIMIZATION IDEA:
list(map(int,input().split())) -> Converts values in list to type int. No need to do forced type conversion further.
"""

nk = input().split()
count = 0

num = input()
x = num.split()
for j in x:
    if int(j) > 0:
        if int(j) >= int(x[int(nk[1])-1]):
            count += 1
print(count)