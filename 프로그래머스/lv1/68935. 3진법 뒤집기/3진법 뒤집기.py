import math
def solution(n):
    answer = ''
    while n>=1:
        i = n%3
        answer += str(i)
        n //= 3
    return int(answer,3)
