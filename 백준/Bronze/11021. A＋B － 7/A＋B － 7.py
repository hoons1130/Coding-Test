n = input()
n = int(n)
for i in range(n):
    n,m = input().split()
    n = int(n)
    m = int(m)
    ans = n + m
    print(f'Case #{i+1}: {ans}')