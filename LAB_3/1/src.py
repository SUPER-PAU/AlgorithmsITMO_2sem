from tests import test_performance


def dfs(graph, start, visited):
    visited[start] = True
    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)


@test_performance
def main():
    with open("test1.txt", 'r') as file:
        n, m = map(int, file.readline().split())
        graph = [[] for _ in range(n + 1)]

        for _ in range(m):
            a, b = map(int, file.readline().split())
            if not (1 <= a <= n and 1 <= b <= n):
                return print(f"Invalid edge: {a} -> {b}")
            graph[a].append(b)
            graph[b].append(a)
        u, v = map(int, file.readline().split())
    file.close()

    # [print(i, "-", *graph[i]) for i in range(n + 1)]

    visited = [False] * len(graph)
    dfs(graph, u, visited)

    if visited[v]:
        print("1")
    else:
        print("0")

if __name__ == '__main__':
    main()
