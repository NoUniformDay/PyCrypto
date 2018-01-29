from crypto import AffineCipher
from crypto import isEnglish

k=AffineCipher
k.setAlphabet('ABCDEFGHIJKLMNOPQRSTUVWXYZ ')
for a in range(1,26):
	for b in range(0,26):
		k.setDecipherKey([a,b])
		txt=k.decipher("cipher.txt")
		if isEnglish(txt):
			print(txt);
			print(" ");

