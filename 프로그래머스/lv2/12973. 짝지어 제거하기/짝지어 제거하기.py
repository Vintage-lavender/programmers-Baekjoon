def solution(s):
    answer = []
    for i in s:
        if answer and answer[-1]==i:
            answer.pop()
        else:
            answer.append(i)
    return int(not answer)