#https://www.hackerrank.com/challenges/py-check-strict-superset/problem
n = int(input())
a = set(map(int, input().split()))
m = int(input())
for _ in range(m):
    operation = input().split()
    b = set(map(int, input().split()))
    if operation[0] == "update":
        a.update(b)
    elif operation[0] == "intersection_update":
        a.intersection_update(b)
    elif operation[0] == "difference_update":
        a.difference_update(b)
    elif operation[0] == "symmetric_difference_update":
        a.symmetric_difference_update(b)
print(sum(a))
