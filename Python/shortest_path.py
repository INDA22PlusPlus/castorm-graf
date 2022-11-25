import math
from queue import PriorityQueue

while True:
    n, m, q, s = map(int, input().split())
    if n == m == q == s == 0:
        exit()
    dp = [math.inf for _ in range(n)]
    dp[s] = 0
    edges = [[0 for _ in range(n)] for _ in range(n)]
    key = [[] for _ in range(n)]
    visited = [False for _ in range(n)]

    for _ in range(m):
        a, b, w = map(int, input().split())
        edges[a][b] = w
        key[a].append(b)

    pq = PriorityQueue()
    curr = s
    while unvisited:
        if curr in unvisited: unvisited.remove(curr)
        for neighbour in edges[curr]:
            dp[neighbour] = min(dp[neighbour], dp[curr] + edges[curr][neighbour])

        best = math.inf
        nxt = None
        for node in unvisited:
            if dp[node] < best:
                best = dp[node]
                nxt = node
        if nxt == None: break
        curr = nxt
        
    
    for _ in range(q):
        e = int(input())
        if dp[e] == math.inf:
            print("Impossible")
        else:
            print(dp[e])
            


