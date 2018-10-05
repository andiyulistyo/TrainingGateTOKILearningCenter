input = input()
a, b = input.split()

n = int(a)
x = int(b)

string = ''
for i in range(n + 1):
    if i != 0:
        if i % x == 0:
            string = string + '*' + ' '
        else:
            string += str(i) + ' '

print(string.rstrip())