n=3
m=4
A = []
for i in range(n):
  B = []
  for j in range(m):
     B.append(int(input()))
  A.append(B)
  

     
print(A)
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

     
print(A)
