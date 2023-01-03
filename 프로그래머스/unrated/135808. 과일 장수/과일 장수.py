def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)
    index = m-1
    while index<(m*(len(score)//m)):
        answer += score[index] * m
        index += m
    return answer