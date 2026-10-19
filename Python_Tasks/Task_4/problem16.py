#https://www.hackerrank.com/challenges/nested-list/problem
if __name__ == '__main__':
    d = {}
    names = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        d[name] = score
    unique = sorted(list(set(d.values())))
    second_score = unique[1]
    for name,score in d.items():
        if score==second_score:
            names.append(name)
    for i in sorted(names):
        print(i)
