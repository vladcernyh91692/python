n=3
A = []
Fin = open ( "Черных Владислав Юрьевич_УБ-22_vvod.txt" )
Fout = open ( "Черных Владислав Юрьевич_УБ-22_vivod.txt", "w" )  

for i in range(n):
  B = []
  s = Fin.readline().split() #Чтение строки и разбивка по пробелам
  for j in range(n):
     B.append(int(s[j]))
  A.append(B)
  
for i in range(n):
  print(A[i])
  
Flag=True
for i in range(n):
  for j in range(n):
      if A[i][j]!=A[j][i]:
          Flag=False
          break
  if Flag==False:
      break
if Flag:
 Fout.write ('Yes'+"\n" )
else:
    Fout.write ('No'+"\n" )
Fin.close()
Fout.close()

    
