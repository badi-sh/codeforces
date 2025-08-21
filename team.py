"""
Create Variable n to control no. of problems to solve

If 1 in i > 2, Sure About Problem. Else Not sure.
If sure, count ++.

NOTE: FOR EVERY LOOP THE LIST IN A LOOP GETS REASSIGNED AS LONG AS IT IS EQUAL TO.

MY CODE [UNOPTIMIZED]:
x = int(input())
count = 0

for i in range(x):
    y = input()
    k = 0
    for j in y:
        if j == " ":
            continue
        k += int(j)
        if k >= 2:
            count += 1
            break
print(count)

PP CODE [SIMPLIFIED]:
x = int(input())
num = 0

for i in range(x):
    y = input()
    if y.count("1") >= 2:
        num += 1

print(num)
"""
# x = int(input())
# count = 0

# for i in range(x):
#     y = input()
#     k = 0
#     for j in y:
#         if j == " ":
#             continue
#         k += int(j)
#         if k >= 2:
#             count += 1
#             break
# print(count)



# Below Gives RUNTIME LIMIT ERROR in CodeForce [MORON MAXXING]
# count = 0            

# mas = int(input())
# for i in range(mas):
#     x = input().split()
#     for j in x:
#         if j == "1":
#             k += 1
#             if k >= 2:
#                 print(k, "k")
#                 count += 1
#                 break

# print(count)

# x = int(input())
# num = 0

# for i in range(x):
#     y = input()
#     if y.count("1") >= 2:
#         num += 1

# print(num)
