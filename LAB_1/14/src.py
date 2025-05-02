from tests import test_performance


def eval_op(a, b, op):
    """
    функция выполняет необходимую операцию между числами `a` и `b` в зависимости от `op`
    """
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b


def min_and_max(i, j, ops, mins, maxs):
    min_val = float('inf')
    max_val = float('-inf')
    for k in range(i, j):
        op = ops[k]
        a = eval_op(maxs[i][k], maxs[k + 1][j], op)
        b = eval_op(maxs[i][k], mins[k + 1][j], op)
        c = eval_op(mins[i][k], maxs[k + 1][j], op)
        d = eval_op(mins[i][k], mins[k + 1][j], op)
        min_val = min(min_val, a, b, c, d)
        max_val = max(max_val, a, b, c, d)
    return min_val, max_val


def get_maximum_value(strg):
    digits = list(map(int, strg[::2]))
    operators = strg[1::2]
    n = len(digits)

    mins = [ [0] * n for _ in range(n) ]
    maxs = [ [0] * n for _ in range(n) ]

    for i in range(n):
        mins[i][i] = digits[i]
        maxs[i][i] = digits[i]

    for s in range(1, n):  # длина подвыражения - 1
        for i in range(n - s):
            j = i + s
            mins[i][j], maxs[i][j] = min_and_max(i, j, operators, mins, maxs)

    return maxs[0][n - 1]


@test_performance
def main():
    with open('test1.txt', 'r', encoding='utf-8') as f:
        strg = f.readline().strip()

    print(get_maximum_value(strg))

if __name__ == '__main__':
    main()