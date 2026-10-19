#https://www.hackerrank.com/challenges/find-a-string/problem
def count_substring(string, sub_string):
    total_count = 0
    idx = 0
    for i in range(len(string)):
        if string[i:i+len(sub_string)]==sub_string:
            total_count+=1
    return total_count
