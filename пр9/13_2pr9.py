n=3
m=4
A = []
Fin = open ( "Черных Владислав Юрьевич_УБ-22_vvod.txt" )
Fout = open ( "Черных Владислав Юрьевич_УБ-22_vivod.txt", "w" )   #режим ("r" – чтение,"w" – запись,"a" – добавление)

for i in range(n):
  B = []
  s = Fin.readline().split() #Чтение строки и разбивка по пробелам
  for j in range(m):
     B.append(int(s[j]))
  A.append(B)
  
for i in range(n):
  print(A[i])  
imax=jmax=imin=jmin=0  
for i in range(n):
  for j in range(m):
      if A[i][j]>A[imax][jmax]:
          imax=i
          jmax=j
      if A[i][j]<A[imin][jmin]:
          imin=i
          jmin=j
A[imax][jmax],A[imin][jmin]=A[imin][jmin],A[imax][jmax]

     
for i in range(n):
  for j in range(m):
    Fout.write ( str(A[i][j])+" ")
  Fout.write ("\n" )

Fin.close()
Fout.close()
