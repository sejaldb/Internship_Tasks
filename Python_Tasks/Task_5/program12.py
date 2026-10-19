#https://www.hackerrank.com/challenges/capitalize/problem
def solve(s):
    result = ""
    for i in range(len(s)):
        if s[i-1]==" " or i==0:
            result += s[i].upper()
        else:
            result += s[i]
    return result
