#몫은 현재 들어갈 숫자와 관련
#나머지는 남은 숫자와 관련
import math
def solution(n, k):
    answer = []
    numlist = [x for x in range(1,n+1)]
    while len(numlist)>=1:
        #print(answer)
        case = math.factorial(n-1)
        if k%case:
            index = k//case
        else: #나누어떨어진다면
            index = (k//case)-1
        answer.append(numlist.pop(index))
        n -= 1
        k %= case
    return answer