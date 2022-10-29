n=3
A = []
for i in range(n):
  B = []
  for i in range(n):
     B.append(int(input()))
  A.append(B)
  
for i in range(n):
  for j in range(n):
     print(A[i][j],end='')
     
  print()
Flag=True
for i in range(n):
  for j in range(n):
      if A[i][j]!=A[j][i]:
          Flag=False
          break
  if Flag==False:
      break
if Flag:
 print('Yes')
else:
    print('No')

    
