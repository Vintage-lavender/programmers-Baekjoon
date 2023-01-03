def solution(t, p):
    p_len = len(p)
    t_len = len(t)
    answer = 0
    for i in range(t_len-p_len+1):
        num = int(t[i:i+p_len])
        if num <= int(p):
            answer += 1 
    return answer