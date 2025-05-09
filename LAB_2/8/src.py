from tests import test_performance

@test_performance
def main():
    with open('test1.txt', 'r', encoding='utf-8') as file:
        n = int(file.readline())
        if n == 0:
            print(0)
            return
        nodes = [None]
        for _ in range(n):
            key, left, right = map(int, file.readline().split())
            nodes.append((left, right))

    #       idx, height
    stack = [(1, 1)]
    max_height = 0

    while stack:
        node_index, height = stack.pop()
        max_height = max(max_height, height)

        left, right = nodes[node_index]
        if left != 0:
            stack.append((left, height + 1))
        if right != 0:
            stack.append((right, height + 1))

    print(max_height)


    def find_height(idx, height):
        if idx == 0:
            return height - 1
        return max(find_height(nodes[idx][0], height + 1), find_height(nodes[idx][1], height + 1))

    print(find_height(1, 1))


if __name__ == "__main__":
    main()
