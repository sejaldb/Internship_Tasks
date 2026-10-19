#https://www.hackerrank.com/challenges/finding-the-percentage/problem
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    add = 0
    for mark in student_marks[query_name]:
        add += mark
    print(f"{add/len(student_marks[query_name]):.2f}")
