#최대한 보트에 두명을 모두 태울 수 있는 방향으로.
#스택
def solution(people, limit):
    from collections import deque
    answer = 0
    #people.sort(reverse=True)
    #queue = deque(map(int,people))
    queue = deque(sorted(people,reverse=True))
    while queue:
        if len(queue)>1 and queue[0]+queue[-1]<=limit:
            queue.pop()
            queue.popleft()
        else:
            queue.popleft()
        answer += 1
    return answer