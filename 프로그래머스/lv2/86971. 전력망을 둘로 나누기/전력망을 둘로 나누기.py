def bfs(graph,start,visited):
    from collections import deque
    nlist = deque()
    cnt = 1
    nlist.append(start)
    while len(nlist)>0:
        now = nlist.pop()
        for i in graph[now]:
            if not visited[i]:
                nlist.append(i)
                visited[i] = True
                cnt += 1
    return cnt

def solution(n, wires):
    #인접리스트 생성
    #숫자가 작은 노드의 연결선이 먼저 주어짐
    #앞노드와의 연결정보는 앞에 모두 나오게 됨
    #한 노드의 연결선을 끊으면 그 노드에서부터 탐색 시작
    answer = n
    graph = [set() for _ in range(n+1)]
    for v1, v2 in wires:
        graph[v1].add(v2)
        graph[v2].add(v1)
    #연결선을 한개씩 끊어봄
    for s1, s2 in wires: #s1과 s2 각각에서 넓이우선 탐색 시작
        graph[s1].remove(s2)
        graph[s2].remove(s1)
        #print(graph)
        visited = [True if i==s1 or i==s2 else False for i in range(n+1)]
        s1t = bfs(graph,s1,visited)
        s2t = bfs(graph,s2,visited)
        answer = min(answer,abs(s1t-s2t))
        #print(s1,s2,abs(s1t-s2t),answer)
        #다시 연결
        graph[s1].add(s2)
        graph[s2].add(s1)
    
    return answer
           
        
    