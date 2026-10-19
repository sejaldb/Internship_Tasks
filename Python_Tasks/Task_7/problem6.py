#https://www.hackerrank.com/challenges/pangrams/problem
s = input().lower()
if len(set(s.replace(" ", ""))) == 26:
    print("pangram")
else:
    print("not pangram")
