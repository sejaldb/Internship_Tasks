#https://www.hackerrank.com/challenges/validating-the-phone-number/problem?utm_source=chatgpt.com
n = int(input())
for _ in range(n):
    number = input()
    if len(number) == 10 and number.isdigit() and number[0] in "789":
        print("YES")
    else:
        print("NO")
