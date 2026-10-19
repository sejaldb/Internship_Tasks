#https://www.hackerrank.com/challenges/weighted-uniform-string/problem
s = input()
n = int(input())
weights = set()
count = 0
previous = ""
for char in s:
    if char == previous:
        count += 1
    else:
        count = 1
    weights.add((ord(char) - ord('a') + 1) * count)
    previous = char
for _ in range(n):
    x = int(input())
    print("Yes" if x in weights else "No")
