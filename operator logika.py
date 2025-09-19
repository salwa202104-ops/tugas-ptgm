#python 3.7.1

a = False
c = not a
print('data a =',a)
print('data c =',c)
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)
a = True
b = False
c = a or b
print(a,'OR',b,'=',c)
a = False
b = False
c = a and b
a = True
b = False
c = a and b
a = True
b = True
c = a and b