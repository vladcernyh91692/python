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
for i in range(n):
    A[i].sort(reverse=True)
print(A)
d=[]
for row in A:
    d.append(row)
d.sort(reverse=True)
print(d)
