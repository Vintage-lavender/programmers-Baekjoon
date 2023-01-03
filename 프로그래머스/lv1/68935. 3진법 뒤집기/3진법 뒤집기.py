import math
def solution(n):
    answer = 0
    highest = int(math.log(n,3))
    while n>=1:
        i = int(math.log(n,3)) #n >= 3**int(i), n이 3보다 작으면 분수나옴. 1일때는 0
        answer += 3**(highest-i)
        n -= 3**i
    return answer