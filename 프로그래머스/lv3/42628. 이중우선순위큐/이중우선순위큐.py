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
        return [max(queue),queue[0]] #minheap의 최댓값은 마지막 인덱스로 보장되지 않음
    return [0,0]