def solution(lottos, win_nums):
    answer = [0,0]
    wlist = [0] * 46
    for w in win_nums:
        wlist[w] = 1
    for i in lottos:
        if wlist[i] == 1 :
            answer[1] += 1
        if i==0:
            answer[0] += 1
    answer[0] += answer[1]
    answer = [7-r if r!=0 else 6 for r in answer]
    return answer