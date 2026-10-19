#https://www.hackerrank.com/challenges/anagram/problem
t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    if n % 2 != 0:
        print(-1)
    else:
        a = s[:n // 2]
        b = s[n // 2:]
        from collections import Counter
        print(sum((Counter(a) - Counter(b)).values()))
