n = int(input())

for _ in range(n):
    a, b = input().split()
    a = int(a)
    ans = ""
    for i in b:
        ans += i*a
    print(ans)