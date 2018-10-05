x = int(input())

if x < 10: 
    print('satuan')
elif x < 100:
    print('puluhan')
elif x < 1000:
    print('ratusan')
elif x < 10000:
    print('ribuan')
else:
    print('puluhribuan')
    