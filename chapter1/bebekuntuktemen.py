inputan = input()
n, m = inputan.split()

bagi = divmod(int(n), int(m)) 
print('masing-masing', bagi[0])
print('bersisa', bagi[1])

