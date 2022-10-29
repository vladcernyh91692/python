import random
N=3
M=4
A = []  
for i in range(N):
  B=[]
  for j in range(M):
     B.append ( random.randint(2, 20))
  A.append (B)

for row in A:
    for x in row:
      print ( "{:4d}".format(x), end = "" )
    print ()

print ('Новая матрица')    
for i in range(N):
                     
    nummin=0
    for j in range(M):
        if A[i][j]<A[i][nummin]:
            nummin=j
    if A[i][nummin]%2==0:
        A[i][nummin]=0
    else:
        A[i][nummin]=1

for row in A:
    for x in row:
      print ( "{:4d}".format(x), end = "" )
    print ()
