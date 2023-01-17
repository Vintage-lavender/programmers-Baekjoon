# *은 직전,현재 점수 2배
# #은 현재 점수 (-1)배
# S: 1제곱, D: 2제곱, T: 3제곱
def solution(dartResult):
    answer = []
    dartResult = list(map(str,dartResult))
    for d in dartResult:
        if d== 'S':
            answer[-1] = int(answer[-1])
        elif d== 'D':
            answer[-1] = int(answer[-1])**2
        elif d== 'T':
            answer[-1] = int(answer[-1])**3
        elif d== '*':
            answer[-1] *= 2
            if len(answer) > 1:
                answer[-2] *= 2
        elif d== '#': 
            answer[-1] = -answer[-1]    
        else:
            if len(answer)>0 and answer[-1]==str(answer[-1]):
                answer[-1] += d
            else:
                answer.append(d)
    #print(answer)
    return sum(answer)