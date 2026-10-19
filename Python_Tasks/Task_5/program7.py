#https://www.hackerrank.com/challenges/symmetric-difference/problem
if __name__ == '__main__':
    M = int(input())
    a = set(map(int, input().split()))
    N = int(input())
    b = set(map(int, input().split()))
    result = sorted(a ^ b)
    for i in result:
        print(i)
