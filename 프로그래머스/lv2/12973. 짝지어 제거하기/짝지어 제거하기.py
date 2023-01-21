def solution(s):
    from collections import deque
    #answer = []
    answer = deque()
    for i in s:
        if answer and answer[-1]==i:
            answer.pop()
        else:
            answer.append(i)
    return int(not answer)