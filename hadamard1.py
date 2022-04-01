import numpy as np
import math
from scipy.linalg import hadamard
import sys



a  =  []
z = [];
plain_list=[]

b = str(input('input string : '))
listb = list(b)
lenb=len(b)

order_list=[]
for i in range (lenb,1000):
    if math.gcd(i,27)==1 :
        ceil = math.ceil(math.log(i,2))
        floor = math.floor(math.log(i,2))
        if ceil == floor:
            order_list.append(i)
            
            
print("daftar order yang mungkin : ",order_list)

    
order = int(input("input matrix order : "))
if math.gcd(order,27)!=1 or order%4!=0:
    print("error order, please input another order")
    sys.exit()

matrix = hadamard(order)
matrix_rows = np.shape(matrix)[0]
det = math.ceil(np.linalg.det(matrix))
inv_matrix = []

w=1
if lenb<=order:
    while w <=order-lenb:
        listb.append(" ")
        w=w+1
else :
    print("ganti order matriks")
    sys.exit()


smallalpha = [" ","a", "b", "c", "d", "e", "f", "g", "h",
              "i", "j", "k", "l", "m", "n", "o", "p", "q",
              "r", "s", "t", "u", "v", "w", "x", "y", "z"]
capitalalpha = [" ","A", "B", "C", "D", "E", "F", "G", "H",
                "I", "J", "K", "L", "M", "N", "O", "P", "Q",
                "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
alphavalues = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
               13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
               23, 24, 25, 26, 27]

for i in range (len(listb)):
  for j in range (27):
    if listb[i]==smallalpha[j]:
      a.append(alphavalues[j])
      if j  == 27 :
        j = 0
        break
    
cipher = (np.matmul(matrix,a))%27

encrypted = ""

for i in range (0,len(cipher)):
    for j in range (27):
        if cipher[i]==alphavalues[j]:
            encrypted =''.join([encrypted,capitalalpha[j]])
            
print("\n encrypted text : "+encrypted)


c = encrypted.lower()
listc = list(c)
lenc= len(c)

for i in range (lenc):
  for j in range (27):
    if listc[i]==smallalpha[j]:
      z.append(alphavalues[j])
      if j  == 27 :
        j = 0
        break
 
for k in range (27):
    if math.gcd(matrix_rows,27)==1:
        if (k*matrix_rows)%27==1:
            inv_det=k    
    else :
        print("matrix has no inverse")
        break

A = np.matrix(matrix)
transpose = A.getH()

inv_matrix = (np.dot(inv_det,transpose))

 
plain = (np.matmul(inv_matrix,z))%27

for x in np.array(plain).flat:
    plain_list.append(x)
    
decrypted = ""

for m in range (0,len(plain_list)):
    for n in range (27):
        if plain_list[m]==alphavalues[n]:
            decrypted =''.join([decrypted,capitalalpha[n]])
            
print("\n decrypted text : "+decrypted)

            
    