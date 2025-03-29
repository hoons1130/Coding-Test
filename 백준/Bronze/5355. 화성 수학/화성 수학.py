n = int(input())

for _ in range(n):
    tokens = input().split()
    num = float(tokens[0])
    
    for op in tokens[1:]:
        if op == '@':
            num *= 3
        elif op == '%':
            num += 5
        elif op == '#':
            num -= 7
            
    print(f"{num:.2f}")