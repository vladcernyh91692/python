a=int(input('Введите целое число:'))
b=int(input('Введите целое число:'))
if (a<2 and b>3) or (a>b and a>3):
      if a<2 and b>3:
           c=a+b*b
           print('c=',c)
      if a>b and a>3:
           c=b*b+2
           print('c=',c)
else:
      c=b
      print('c=',c)
