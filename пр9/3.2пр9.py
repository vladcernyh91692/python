n=3
A = []
Fin = open ( "Черных Владислав Юрьевич_УБ-22_vvod.txt" )
Fout = open ( "Черных Владислав Юрьевич_УБ-22_vivod.txt", "w" )   #режим ("r" – чтение,"w" – запись,"a" – добавление)

for i in range(n):
  B = []
  s = Fin.readline().split() #Чтение строки и разбивка по пробелам
  for j in range(n):
     B.append(int(s[j]))
  A.append(B)
  
for i in range(n):
  print(A[i])

maxi=0  # поиск наибольшего
maxj=0
for i in range(n):
  for j in range(n):
    if A[i][j]>A[maxi][maxj]:
      maxi=i #это номер строки
      maxj=j

     
#перестановка строк
for i in range(n):
  A[0][i],A[maxi][i]=A[maxi][i],A[0][i]

    #перестановка столбцов
for i in range(n):
  A[i][0],A[i][maxj]=A[i][maxj],A[i][0]

for i in range(n):
  for j in range(n):
    Fout.write ( str(A[i][j])+" ")
  Fout.write ("\n" )

Fin.close()
Fout.close()
