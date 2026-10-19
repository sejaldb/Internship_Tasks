#https://www.hackerrank.com/challenges/py-set-difference-operation/problem
if __name__ == '__main__':
    n = int(input())
    a = set(input().split())
    m = int(input())
    b = set(input().split())
    print(len(a.difference(b)))
