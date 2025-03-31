import sys 
n = int(sys.stdin.readline())
lst = []

for _ in range(n):
    temp = sys.stdin.readline().split()

    if temp[0] == '1':
        lst.append(int(temp[1]))

    elif temp[0] == '2':
        if not lst:
            print(-1)
        else:
            print(lst.pop())

    elif temp[0] == '3':
        print(len(lst))

    elif temp[0] == '4':
        print(1 if not lst else 0)

    elif temp[0] == '5':
        if not lst:
            print(-1)
        else:
            print(lst[-1])
