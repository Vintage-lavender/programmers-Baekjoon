#큐가 비어있으면 [0,0]
import heapq
def solution(operations):
    queue = []
    for o in operations:
        operation, num = o.split()
        if operation == 'I':
            heapq.heappush(queue, int(num))

        elif len(queue)>=1:
            if num == '-1':
                heapq.heappop(queue)
            else:
                queue.pop()
        #print(queue)
    
    if len(queue) >= 1:
        return [max(queue),queue[0]]
    return [0,0]