#패턴
#1. 1,2,3,4,5
#2. 2,1,2,3,2,4,2,5
#3. 3,3,1,1,2,2,4,4,5,5
from itertools import cycle
def solution(answers):
    fstud = cycle([1,2,3,4,5])
    sstud = cycle([2,1,2,3,2,4,2,5])
    tstud = cycle([3,3,1,1,2,2,4,4,5,5])
    cnt = [0] * 3
    for a in answers:
        if a == next(fstud):
            cnt[0] += 1
        if a == next(sstud):
            cnt[1] += 1
        if a == next(tstud):
            cnt[2] += 1
    maxvalue = max(cnt)
    final = []
    for i,c in enumerate(cnt):
        if maxvalue == c:
            final.append(i+1)
    return final