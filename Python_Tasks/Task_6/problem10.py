#Designer door mat
#https://www.hackerrank.com/challenges/designer-door-mat/problem
if __name__ == '__main__':
    n, m = map(int, input().split())
    for i in range(n // 2):
        print(('.|.' * (2 * i + 1)).center(m, '-'))
    print('WELCOME'.center(m, '-'))
    for i in range(n // 2 - 1, -1, -1):
        print(('.|.' * (2 * i + 1)).center(m, '-'))
