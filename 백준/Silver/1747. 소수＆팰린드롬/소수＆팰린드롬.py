import math

def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

x = int(input())

for i in range(x, 1003002): 
    if str(i) == str(i)[::-1]:  
        if isprime(i):         
            print(i)
            break