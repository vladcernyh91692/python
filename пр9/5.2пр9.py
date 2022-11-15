import random
N=3
M=4
A = []  
Fin = open ( "Черных Владислав Юрьевич_УБ-22_vvod.txt" )
Fout = open ( "Черных Владислав Юрьевич_УБ-22_vivod.txt", "w" )   #режим ("r" – чтение,"w" – запись,"a" – добавление)

for i in range(N):
  B = []
  s = Fin.readline().split() #Чтение строки и разбивка по пробелам
  for j in range(M):
     B.append(int(s[j]))
  A.append(B)

for i in range(N):
  print(A[i]) 

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

for i in range(N):
  for j in range(M):
    Fout.write ( str(A[i][j])+" ")
  Fout.write ("\n" )

Fin.close()
Fout.close()
