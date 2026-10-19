#https://www.hackerrank.com/challenges/separate-the-numbers/problem
n = int(input())
s = input()
k = int(input()) % 26
result = ""
for char in s:
    if char.islower():
        result += chr((ord(char) - ord('a') + k) % 26 + ord('a'))
    elif char.isupper():
        result += chr((ord(char) - ord('A') + k) % 26 + ord('A'))
    else:
        result += char
print(result)
