def solution(n):
    answer = ''
    nlist = sorted(map(str,str(n)),reverse=True)
    for i in nlist:
        answer += i
    return int(answer)