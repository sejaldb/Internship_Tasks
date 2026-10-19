#https://www.hackerrank.com/challenges/py-check-strict-superset/problem
a = set(input().split())
n = int(input())
result = True
for _ in range(n):
    b = set(input().split())
    if not a > b:
        result = False
print(result)
