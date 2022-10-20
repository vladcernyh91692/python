n=int(input())
a=[]
b=[]
for i in range(n):
    
    a.append(int(input()))

for i in range(n):
    if (a[i]%2==0)and (a[i]<10):
        b.append(a[i])
print('a:',a)
if len(b)==0:
    print('Таких элементов нет')
else:
    print('b:',b)
