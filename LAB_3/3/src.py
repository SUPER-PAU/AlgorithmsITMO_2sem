from tests import test_performance

has_cycle = False

def dfs(graph, start, visited):
    global has_cycle
    visited[start] = 1
    for neighbor in graph[start]:
        if visited[neighbor] == 0:
            dfs(graph, neighbor, visited)
        elif visited[neighbor] == 1:
            has_cycle = True

    visited[start] = 2


@test_performance
def main():
    global has_cycle
    with open("test2.txt", 'r') as file:
        n, m = map(int, file.readline().split())
        graph = [[] for _ in range(n + 1)]

        for _ in range(m):
            a, b = map(int, file.readline().split())
            graph[a].append(b)
        file.close()

    # [print(i, "->", *graph[i]) for i in range(1, n + 1)]

    visited = [0] * len(graph)

    for i in range(1, n + 1):
        if visited[i] == 0:
            dfs(graph, i, visited)

    if has_cycle:
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    main()
