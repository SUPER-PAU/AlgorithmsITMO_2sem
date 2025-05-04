from tests import test_performance
from acycle_as_func import check_cycle


def dfs(graph, start, visited, result):
    visited[start] = True
    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, result)
    result.append(start)


@test_performance
def main():
    with open("test4.txt", 'r') as file:
        n, m = map(int, file.readline().split())
        graph = [[] for _ in range(n + 1)]

        for _ in range(m):
            a, b = map(int, file.readline().split())
            if not (1 <= a <= n and 1 <= b <= n):
                return print(f"Invalid edge: {a} -> {b}")
            graph[a].append(b)
        file.close()

    # [print(i, "->", *graph[i]) for i in range(1, n + 1)]

    if check_cycle(graph):
        print("Cycle found")
        return False

    visited = [False] * len(graph)
    result = []

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(graph, i, visited, result)
    result.reverse()
    print(*result)


if __name__ == '__main__':
    main()
