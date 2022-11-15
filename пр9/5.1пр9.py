n=3
m=4
A=[]
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
print()
  
for i in range(n):
   A[i].sort()
   

  
for i in range(n):
  for j in range(n):
    Fout.write ( str(A[i][j])+" ")
  Fout.write ("\n" )

Fin.close()
Fout.close()
