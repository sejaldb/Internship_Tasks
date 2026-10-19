#https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
from collections import Counter
s = input()
freq = list(Counter(s).values())
counts = Counter(freq)
if len(counts) == 1:
    print("YES")
elif len(counts) == 2:
    a, b = sorted(counts.items())
    if a[0] == 1 and a[1] == 1:
        print("YES")
    elif b[0] == a[0] + 1 and b[1] == 1:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
