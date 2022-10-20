def nod(a,b):#алгоритм Эвклида
  while a!=0 and b!=0:
    if a>b:
        a=a%b
    else:
        b=b%a
  if a==0:
    return (b)
  else:
    return (a)

a=int(input())
b=int(input())
print(nod(a,b))
print("nok",int(a*b/nod(a,b)))
