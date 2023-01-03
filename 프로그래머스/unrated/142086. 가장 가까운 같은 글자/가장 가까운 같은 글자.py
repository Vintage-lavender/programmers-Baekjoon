def solution(s):
    answer = []
    alpha = {}
    for i in range(len(s)): 
        tmp = -1
        if s[i] in alpha: 
            tmp = i-alpha[s[i]]
        answer.append(tmp)
        alpha[s[i]] = i 
    return answer