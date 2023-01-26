#애초에 짝이 안맞으면 불가함
#'(','[','{' 찾고 끝나는 지점 찾기
#덩어리시작할 때마다 스택 만들기
#'}]()}}{{[{'
def solution(s):
    from collections import deque
    answer = 0
    squeue = deque(list(map(str,s)))
    dic = {')':'(','}':'{',']':'['}
    for _ in range(len(s)-1):
        stack = deque()
        for i in squeue:
            if not stack:
                stack.append(i)
            elif i in {')','}',']'} and stack[-1]==dic[i]:
                stack.pop()
            else:
                stack.append(i)
        answer += not stack
        first = squeue.popleft()
        squeue.append(first)
    return answer
    
    