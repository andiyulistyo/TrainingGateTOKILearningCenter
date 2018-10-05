x = int(input())

string = ''

for i in range(x):
    for j in range(x):
        if (i + 1) * (j + 1) == x:
            string += str(i + 1) + '\n'

answer = string.split()

for x in answer[::-1]:
    print(x.rstrip())