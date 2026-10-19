#https://www.hackerrank.com/challenges/most-commons/problem
from collections import Counter
s = input()
count = Counter(s)
for char, frequency in sorted(count.items(), key=lambda x: (-x[1], x[0]))[:3]:
    print(char, frequency)
