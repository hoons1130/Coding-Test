A =['c=', 'c-', 'dz=', 'd-', 'lj', 'nj','s=','z=']
n = input()
for i in A:
    n = n.replace(i, '*')
print(len(n))