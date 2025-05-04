from tests import test_performance

def dfs(graph, start, visited):
    visited[start] = True
    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)


@test_performance
def main():
    with open("test2.txt", 'r') as file:
        n, m = map(int, file.readline().split())
        graph = [[] for _ in range(n + 1)]

        for _ in range(m):
            a, b = map(int, file.readline().split())
            graph[a].append(b)
            graph[b].append(a)
    file.close()

    # [print(i, "-", *graph[i]) for i in range(1, n + 1)]

    visited = [False] * len(graph)

    count = 0
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(graph, i, visited)
            count += 1
    print(count)

if __name__ == '__main__':
    main()
