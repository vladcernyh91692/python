n=int(input())
a=[]
for i in range(n):
    
    a.append(int(input()))
max=1
for i in range(n):
    if (a[i]%2==0):
        max=a[i]
        break
for j in range(i+1,n):
    if (a[j]%2==0)and (a[j]>max):
       max=a[j]
print('a:',a)
if max!=1:
   print(max)
else:
    print('Четных элементов нет')
