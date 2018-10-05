import sys

data = sys.stdin.readlines() 

result = 0
for x in data:
    result = int(x) + result 

print(result)