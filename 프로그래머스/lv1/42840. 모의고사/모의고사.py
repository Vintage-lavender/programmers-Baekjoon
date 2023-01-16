#패턴
#1. 1,2,3,4,5
#2. 2,1,2,3,2,4,2,5
#3. 3,3,1,1,2,2,4,4,5,5
def solution(answers):
    qnum = len(answers)
    fstud = [1,2,3,4,5] * (qnum//5+1)
    sstud = [2,1,2,3,2,4,2,5] * (qnum//8+1)
    tstud = [3,3,1,1,2,2,4,4,5,5] * (qnum//10+1)
    cnt = {1:0,2:0,3:0}
    for i in range(qnum):
        if answers[i] == fstud[i]:
            cnt[1] += 1
        if answers[i] == sstud[i]:
            cnt[2] += 1
        if answers[i] == tstud[i]:
            cnt[3] += 1
    cnt = sorted(cnt.items(),key=lambda x: x[1],reverse=True)
    minvalue = cnt[0][1]
    final = []
    for i,c in cnt:
        if minvalue == c:
            final.append(i)
        else:
            return final
    return final