import heapq
import sys

input = sys.stdin.readline

n, m, x = map(int, input().split())
INF = int(1e9)

graph = [[] for i in range(n+1)]

for _ in range(m):
    v1, v2, t = map(int, input().split())
    graph[v1].append((v2,t))

def dijkstra(x):
    queue = []
    heapq.heappush(queue, (0,x)) # 시작노드 -> 시작노드 소요시간은 0
    times[x] = 0
    while queue:
        time, now = heapq.heappop(queue) # x~now까지 가장 소요시간이 적은 경로
        if times[now] < time: # 이전 경로가 최단 경로일 때는 스킵
            continue
        # 최단 경로가 아니였을 경우 now 정점과 인접한 모든 정점의 최단 경로 갱신
        for i in graph[now]:
            cost = time + i[1]
            if cost < times[i[0]]:
                times[i[0]] = cost
                heapq.heappush(queue,(cost,i[0])) # 최단 경로 갱신
    return times

go = [0] *(n+1) # 각 학생들이 x까지 가는데 걸리는 최단 시간

for i in range(1,n+1):
    times = [INF] * (n+1)
    times[0] = 0
    if i!=x:
        go[i] += dijkstra(i)[x]
    else:
        back = dijkstra(i)

print(max([g + b for g, b in zip(go,back)]))