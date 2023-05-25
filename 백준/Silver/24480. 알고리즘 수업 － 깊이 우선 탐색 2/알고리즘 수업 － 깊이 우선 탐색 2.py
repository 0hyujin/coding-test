import sys

sys.setrecursionlimit(10 ** 8)


def dfs(v):
    global cnt
    visited[v] = True

    # 4번은 2번째 방문, 3번은 3번째 방문, 2번은 4번째 방문
    # 카운트는 1씩 증가하는데.. 2번째일 때, 4번을 방문하므로, answer[4] = 2와 같다.
    answer[v] = cnt
    # 내림차순 정렬
    graph[v].sort(reverse=True)
    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            dfs(i)


n, m, r = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
answer = [0] * (n + 1)
cnt = 1

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(r)

for val in answer[1:]:
    print(val)