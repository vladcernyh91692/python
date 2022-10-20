def kol(a,b,c,n):
    k=0
    s=[a,b,c]# набор-цифры допустимые
    
    for i in range(100,n+1):
        
        z1=str(i%10) #последняя цифра числа
        z2=str((i%100)//10)
        z3=str((i%1000)//100)#первая цифра числа
        
        if ((z1 in s) and (z2 in s)and (z3 in s)):
            k+=1
            print(i)
    return (k)

a=input()
b=input()
c=input()

n=int(input())# число из диапазона (210,231)
print(kol(a,b,c,n))


