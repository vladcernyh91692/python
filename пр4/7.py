n=int(input())
sum=0 
for i in range(1,n+1):
     pr=1
     for j in range(1,i+1):
         pr*=j
         
     sum+=pr
print(sum)     
