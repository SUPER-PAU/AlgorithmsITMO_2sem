import sys
from tests import test_performance


sys.setrecursionlimit(10**6)


def in_order(tree):
    result = []
    def dfs(i):
        if i == -1:
            return
        dfs(tree[i][1])
        result.append(tree[i][0])
        dfs(tree[i][2])
    dfs(0)
    return result


def pre_order(tree):
    result = []
    def dfs(i):
        if i == -1:
            return
        result.append(tree[i][0])
        dfs(tree[i][1])
        dfs(tree[i][2])
    dfs(0)
    return result

def post_order(tree):
    result = []
    def dfs(i):
        if i == -1:
            return
        dfs(tree[i][1])
        dfs(tree[i][2])
        result.append(tree[i][0])
    dfs(0)
    return result


@test_performance
def main():
    tree = []
    with open('test2.txt', 'r', encoding='utf-8') as file:
        n = int(file.readline().strip())
        for _ in range(n):
            key, left, right = map(int, file.readline().split())
            tree.append((key, left, right))
    file.close()

    print(*in_order(tree))
    print(*pre_order(tree))
    print(*post_order(tree))


if __name__ == "__main__":
    main()
