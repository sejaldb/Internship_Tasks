#https://www.hackerrank.com/challenges/word-order/problem
if __name__ == '__main__':
    result = {}
    n = int(input())
    for i in range(n):
        word = input()
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    print(len(result))
    print(*result.values())
