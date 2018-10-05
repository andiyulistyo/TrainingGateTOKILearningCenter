n = int(input())

string = ""
printbintang = ""
baris = n

while baris > 0:
	kolom = baris - 1
	while kolom > 0:
		string = string + " "
		kolom = kolom -1

	bintang = 1
	while bintang <= (n - (baris -1)):
		string = string + '*'
		bintang = bintang + 1 
	
	if baris > 1:
		string = string + '\n' 	
	elif baris == 0:
		string += string

	baris = baris - 1

print(string) 
