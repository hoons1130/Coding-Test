a,b,c = input().split()
d= int(input())
a = int(a)
b = int(b)
c = int(c)

c += d
if c >= 60:
    b += c // 60
    c %= 60
    
if b >= 60:
    a = (a + b // 60) %24
    b %= 60

print(a, b, c)