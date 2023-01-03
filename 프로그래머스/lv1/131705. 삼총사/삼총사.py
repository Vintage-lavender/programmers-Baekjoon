def solution(number):
    answer = 0
    p = len(number)
    for i in range(p-2):
        for j in range(i+1,p-1):
            for k in range(j+1,p):
                if number[i]+number[j]+number[k]==0:
                    answer += 1
    return answer