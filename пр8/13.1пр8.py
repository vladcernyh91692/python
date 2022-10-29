n=4
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
b=[]
for i in range(n):
    if i%2!=0:
        b.append(min(A[i]))
print(b)                 
