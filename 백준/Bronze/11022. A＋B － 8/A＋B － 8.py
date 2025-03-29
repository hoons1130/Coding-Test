n= int(input())
for i in range(n):
    n,m = input().split()
    n = int(n)
    m = int(m)
    ans = n+m
    print("Case #{}: {} + {} = {}".format(i+1, n, m ,ans))