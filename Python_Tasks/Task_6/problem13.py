#https://www.hackerrank.com/challenges/py-set-union/problem
n = int(input())
a = set(input().split())

m = int(input())
b = set(input().split())

print(len(a.union(b)))
