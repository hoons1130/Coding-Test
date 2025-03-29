A,B = input().split()
a =int(A)
b= int(B)
c = int(input())
d = b + c 
if d >=60:
    a = (a + d//60) % 24
    b = d % 60
    print(a, b)
else:
    print(a, d)