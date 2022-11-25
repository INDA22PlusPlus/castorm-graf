import math

while True:
    n, m, q = map(int, input().split())
    if n == m == q == 0:
        exit()
        
    distance = [[math.inf for _ in range(n)] for _ in range(n)]

    for i in range(n):
        distance[i][i] = 0

    for i in range(m):
        u, v, w = map(int, input().split())
        distance[u][v] = min(w, distance[u][v])

    for k in range(n):
        for a in range(n):
            for b in range(n):
                distance[a][b] = min(distance[a][b], distance[a][k] + distance[k][b])

    for k in range(n):
        for a in range(n):
            for b in range(n):
                if distance[a][k] + distance[k][b] < distance[a][b]:
                    distance[a][b] = -math.inf

    for _ in range(q):
        u, v = map(int, input().split())
        val = distance[u][v]
        if val == math.inf:
            print("Impossible")
        elif val == -math.inf:
            print("-Infinity")
        else:
            print(val)
