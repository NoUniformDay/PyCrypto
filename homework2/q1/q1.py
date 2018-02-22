################################
#
# Eric McEvoy - Cryptography
# Python script that cracks
# cipher text encrypted with Hill substitution cipher
#
################################

from cs402 import AffineCipher
from cs402 import Alphabet27
from cs402 import isEnglish
from numpy import mat 
from numpy import linalg

afc=AffineCipher
afc.setAlphabet(Alphabet27)

for a in range(1,27):
	for b in range(0,27):
	    for c in range(0,27):
        	for d in range(1,27):
           		matA = mat([[a,b],[c,d]])
           		# print(a); print(""); print(b); print(""); print(c); print(""); print(d); print("");
           		# check matrix is invertible ; determinant does not equal zero
           		detA = a*d - b*c 
	    		if detA != 0:
	    			print("determinant of A : ",detA)
	    			inverse = linalg.inv(matA) #invert the matrix
	    			afc.setDecipherKey(inverse) #deciphering key is the invertible matrix
            		txt=afc.decipher("cipher.txt")
            		print(txt)
            		print(a); print(""); print(b); print(""); print(c); print(""); print(d); print("");
            		if isEnglish(txt): 
                		print("---------Found it! Inverse works ---------"); print(a); print(""); print(b); print(""); print(c); print(""); print(d); print("");
                		break
			
					
              	