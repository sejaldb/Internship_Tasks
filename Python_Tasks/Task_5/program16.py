#https://www.hackerrank.com/challenges/collections-counter/problem
if __name__ == '__main__':
    profit = 0
    X = int(input())
    sizes = input().split()
    N = int(input())
    for _ in range(N):
        customer = input().split() #0 size #1 price
        if customer[0] in sizes:
            profit += int(customer[1])
            sizes.remove(customer[0])
    print(profit)
  #or
  from collections import Counter
if __name__ == '__main__':
    X = int(input())
    sizes = Counter(map(int, input().split()))
    N = int(input())
    profit = 0
    for _ in range(N):
        size, price = map(int, input().split())
        if sizes[size] > 0:
            profit += price
            sizes[size] -= 1
    print(profit)
