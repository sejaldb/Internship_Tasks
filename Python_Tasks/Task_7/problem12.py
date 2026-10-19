#https://www.hackerrank.com/challenges/making-anagrams/problem
from collections import Counter
a = Counter(input())
b = Counter(input())
print(sum((a - b).values()) + sum((b - a).values()))
