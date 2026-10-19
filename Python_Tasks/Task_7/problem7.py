#https://www.hackerrank.com/challenges/alphabet-rangoli/problem
import string
n = int(input())
letters = string.ascii_lowercase
for i in range(n - 1, -n, -1):
    row = letters[abs(i):n]
    print("-".join(row + row[-2::-1]).center(4 * n - 3, "-"))
