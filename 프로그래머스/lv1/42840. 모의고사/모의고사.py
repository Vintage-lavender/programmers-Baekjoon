#패턴
#1. 1,2,3,4,5
#2. 2,1,2,3,2,4,2,5
#3. 3,3,1,1,2,2,4,4,5,5
from itertools import cycle
def solution(answers):
    stud = [cycle([1,2,3,4,5]),
            cycle([2,1,2,3,2,4,2,5]),
            cycle([3,3,1,1,2,2,4,4,5,5])]
    cnt = [0] * 3
    for a in answers:
        for i in range(3):
            if a == next(stud[i]):
                cnt[i] += 1
    maxvalue = max(cnt)
    final = []
    for i,c in enumerate(cnt):
        if maxvalue == c:
            final.append(i+1)
    return final