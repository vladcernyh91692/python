n=3
m=4
A=[]
for i in range(n):
        B=[]
        for j in range(m):
	        B.append(int(input()))
        A.append(B)
for i in range(n):
        for j in range(m):
                print(A[i][j],end=' ')
        print()		
for i in A:
    print('Сортированный массив:',*sorted(i))

