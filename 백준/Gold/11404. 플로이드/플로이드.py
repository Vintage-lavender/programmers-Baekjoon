import heapq
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)

graph = [[INF] * (n+1) for i in range(n+1)]

for _ in range(m):
    v1, v2, t = map(int, input().split())
    graph[v1][v2]=min(t,graph[v1][v2]) # v1에서 v2로 가는 경로는 여러개 일 수 있으므로 최단 거리를 저장

def dijkstra(x):
    queue = []
    heapq.heappush(queue, (0,x)) 
    times[x] = 0
    while queue:
        time, now = heapq.heappop(queue) # x~now까지 가장 소요시간이 적은 경로
        if times[now] < time: # 이전 경로가 최단 경로일 때는 스킵
            continue
        # 최단 경로가 아니였을 경우 now 정점과 인접한 모든 정점의 최단 경로 갱신
        for v,t in enumerate(graph[now]):
            cost = time + t
            if cost < times[v]:
                times[v] = cost
                heapq.heappush(queue,(cost,v)) # 최단 경로 갱신
    return times

for i in range(1,n+1):
    times = [INF] * (n+1)
    times[0] = 0
    tmp = dijkstra(i)
    for i,num in enumerate(tmp):
      if num==INF:
        num = 0  
      if i==(n):
        print(num)
      elif i>0:
        print(num, end=' ')