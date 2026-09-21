#1

n, k = map(int, input("Enter N and K: ").split())
arr = list(map(int, input("Enter array elements: ").split()))

window_sum = sum(arr[:k])
max_sum = window_sum

for i in range(k, n):
    window_sum = window_sum + arr[i] - arr[i - k]
    max_sum = max(max_sum, window_sum)

print("Maximum sum:", max_sum)

#2
s = input("Enter string: ")

seen = set()
left = 0
max_length = 0

for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left += 1

    seen.add(s[right])
    max_length = max(max_length, right - left + 1)

print("Length of longest substring:", max_length)

#3

n, m, k = map(int, input("Enter N, M and K: ").split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

INF = float('inf')
dp = [[INF] * (k + 1) for _ in range(n + 1)]

dp[1][0] = 0

for edges in range(k):
    for u in range(1, n + 1):
        if dp[u][edges] == INF:
            continue

        for v, w in graph[u]:
            dp[v][edges + 1] = min(
                dp[v][edges + 1],
                dp[u][edges] + w
            )

answer = min(dp[n])

if answer == INF:
    print(-1)
else:
    print("Minimum path weight:", answer)