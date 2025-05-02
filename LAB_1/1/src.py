from tests import test_performance


@test_performance
def main():
    with open('test1.txt', 'r', encoding='utf-8') as file:
        n, total_weight = map(int, file.readline().split())
        items = [tuple(map(int, file.readline().split())) for _ in range(n)]

    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0
    for value, weight in items:
        if total_weight == 0:
            break
        if weight <= total_weight:
            total_value += value
            total_weight -= weight
        else:
            total_value += value * (total_weight / weight)
            break


    print(f"{total_value:.4f}")

if __name__ == '__main__':
    main()
