#https://www.hackerrank.com/challenges/game-of-thrones/problem
from collections import Counter
s = input()
odd = 0
for count in Counter(s).values():
    if count % 2 != 0:
        odd += 1
print("YES" if odd <= 1 else "NO")
