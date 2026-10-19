#https://www.hackerrank.com/challenges/piling-up/problem
from collections import deque
for _ in range(int(input())):
    n = int(input())
    cubes = deque(map(int, input().split()))
    top = float('inf')
    while cubes:
        if cubes[0] >= cubes[-1]:
            biggest = cubes.popleft()
        else:
            biggest = cubes.pop()
        if biggest > top:
            print("No")
            break
        top = biggest
    else:
        print("Yes")
