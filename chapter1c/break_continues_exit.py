n = int(input())

number = 1

for number in range(n+1):
    if number == 93:
        print('ERROR')
        break
    elif number % 10 != 0:
        print(number)