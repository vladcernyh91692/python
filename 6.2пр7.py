
from math import * 
def tr(a,b,c):
 p=(a+b+c)/2
 return(sqrt(p*(p-a)*(p-b)*(p-c)))
        
a=int(input())
b=int(input())
c=int(input())
d=int(input())
diag=int(input())
print(tr(a,b,diag)+ tr(c,d,diag))       
