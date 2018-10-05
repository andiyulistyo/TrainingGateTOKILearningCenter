n = int(input())

count = 0
string = ""
index = 0

while count <= n:
    for i in range(count):
        string = string + str(index)
        index += 1

        if index > 9:
            index = 0 
 
    string = string + "\n" 
    count += 1

answer = string.split('\n',1)[1:]
for a in answer:
    print(a.rstrip()) 