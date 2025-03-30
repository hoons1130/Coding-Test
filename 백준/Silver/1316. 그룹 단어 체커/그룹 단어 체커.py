n = int(input())
count = 0
for _ in range(n):
    word = input()
    seen = set()
    prev = ''
    group = True
    for ch in word:
        if ch != prev:
            if ch in seen:
                group = False
                break
            seen.add(ch)
        prev =ch
    if group == True:
        count += 1
        
print(count)
                
            