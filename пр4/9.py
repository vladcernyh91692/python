n=int(input())
a=1 #первые два числа последовательности
b=1
sum=0
for i in range(1,n+1):
    if i==1 or i==2:
       sum+=1
    else:
        c=a+b     #очередное число
        print(c) 
        sum+=c
        a=b
        b=c
print(sum)        
     
