from tests import test_performance

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def append_tree(node, value):
    if node is None:
        return Node(value)
    if value < node.value:
         node.left = append_tree(node.left, value)
    else:
        node.right = append_tree(node.right, value)
    return node


def find_min(node, x):
    if node is None:
        return float("inf")
    if x >= node.value:
        return find_min(node.right, x)
    if x < node.value:
        return min(node.value, find_min(node.left, x))


@test_performance
def main():
    head = None
    with open('test1.txt', 'r', encoding='utf-8') as file:
        for line in file:
            oper, val = line.split()
            val = int(val)
            if oper == '+':
                head = append_tree(head, val)
            else:
                val = find_min(head, val)
                if val == float('inf'):
                    print(0)
                else:
                    print(val)



if __name__ == '__main__':
    main()