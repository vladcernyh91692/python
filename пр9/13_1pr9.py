n=4
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

b=[]
for i in range(n):
    if i%2!=0:
        b.append(min(A[i]))
for i in b:
     Fout.write ( str(i)+" ")
Fout.write ("\n" ) #Выводим как строку

for i in b:
     Fout.write ( str(i))
     Fout.write ("\n" ) #Выводим как столбец
Fin.close()
Fout.close()
       
