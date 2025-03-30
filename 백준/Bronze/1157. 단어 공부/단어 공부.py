n = input().lower()
counter ={}

for letter in n:
    counter[letter] = counter.get(letter, 0) + 1
max_c = max(counter.values())
most = [k for k,v in counter.items() if v == max_c]

if len(most) > 1:
    print("?")
else:
    print(most[0].upper())