import sys

# 크루스칼 알고리즘
def find_parent(parent,x):
    if parent[x] != x: # 루트 노드가 아닐 때
        parent[x] = find_parent(parent, parent[x]) # 부모 노드의 루트노드 찾기
    return parent[x] # 루트 노드 반환

def union_parent(parent,a,b):
    a = find_parent(parent,a) # a의 루트노드
    b = find_parent(parent,b) # b의 루트노드
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

input = sys.stdin.readline

# 0~10만
n = int(input())
parent = [i for i in range(n)] # 자기자신을 루트노드로 초기화

edges = []
result = 0

x=[]
y=[]
z=[]

# -10^9~10^9
for i in range(n):
    x_,y_,z_ = map(int,input().split())
    x.append((x_,i))
    y.append((y_,i))
    z.append((z_,i))

# 오름차순 정렬을 통해 축 내에서의 최단경로 구하기 & 정점 간 거리가 음수가 되는 것 방지
x.sort()
y.sort()
z.sort()

# 축 별로 n-1개의 간선 저장
for i in range(n-1):
    edges.append((x[i+1][0]-x[i][0],x[i][1],x[i+1][1]))
    edges.append((y[i+1][0]-y[i][0],y[i][1],y[i+1][1]))
    edges.append((z[i+1][0]-z[i][0],z[i][1],z[i+1][1]))

edges.sort() # 모든 축의 간선을 오름차순 정렬

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b): # 사이클이 없을 경우에만
        union_parent(parent, a, b)
        result += cost

print(result)