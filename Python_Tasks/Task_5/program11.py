#https://www.hackerrank.com/challenges/text-wrap/problem
import textwrap

def wrap(string, max_width):
    l = []
    for i in range(0,len(string),max_width):
        l.append(string[i:i+max_width])
    return "\n".join(l)
