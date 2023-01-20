from collections import deque
def solution(arr):
    answer = deque()
    answer.append(arr[0])
    for i in arr[1:]:
        if answer[-1]!=i:
            answer.append(i)
    return list(answer)