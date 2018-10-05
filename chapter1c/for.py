list = [int(x) for x in input().split()]

bebek = 0
del list[0]

for i in list:
    if i != 0:
        bebek = bebek + i

print(bebek)    