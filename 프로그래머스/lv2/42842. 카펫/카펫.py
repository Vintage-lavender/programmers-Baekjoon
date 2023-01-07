def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for h in range(3,int(total**0.5)+1): #세로 길이만 탐색
        if total%h == 0:
            w = total//h
            if (w-2)*(h-2) == yellow:
                answer += [w,h]
                break
    return answer