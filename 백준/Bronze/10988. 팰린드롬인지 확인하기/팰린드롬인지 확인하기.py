n = input()
m = ""
for i in range(len(n)-1,-1,-1):
    m = m + n[i]
if n == m:
    print(1)
else:
    print(0)