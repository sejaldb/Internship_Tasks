#https://www.hackerrank.com/challenges/gem-stones/problem
n = int(input())
common = set(input())
for _ in range(n - 1):
    common = common.intersection(set(input()))
print(len(common))
