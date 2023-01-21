#최대한 보트에 두명을 모두 태울 수 있는 방향으로.
def solution(people, limit):
    '''
    #우선순위 큐
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
    '''
    #투 포인터
    answer = 0
    people.sort()
    i = 0
    j = len(people)-1
    while i<j:
        if people[i]+people[j] <= limit:
            answer += 1 #둘이 같이 탈 수 있는 경우
            i += 1
        j -= 1
    return len(people)-answer #전체 사람 수 중에서 둘이 같이타는 경우 빼기