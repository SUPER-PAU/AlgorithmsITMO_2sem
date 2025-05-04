has_cycle = False


def dfs(start, visited, graph):
    global has_cycle
    visited[start] = 1
    for neighbor in graph[start]:
        if visited[neighbor] == 0:
            dfs(neighbor, visited, graph)
        elif visited[neighbor] == 1:
            has_cycle = True

    visited[start] = 2


def check_cycle(graph):
    visited = [0] * len(graph)


    for i in range(1, len(graph)):
        if visited[i] == 0:
            dfs(i, visited, graph)

    return has_cycle

