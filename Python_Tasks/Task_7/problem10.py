#https://www.hackerrank.com/challenges/camelcase/problem
s = input()
count = 1
for char in s:
    if char.isupper():
        count += 1
print(count)
