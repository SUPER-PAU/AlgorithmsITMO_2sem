from tests import test_performance


@test_performance
def main():
    with open('test1.txt', 'r', encoding='utf-8') as file:
        n = int(file.readline())
        a = list(map(int, file.readline().split()))
        b = list(map(int, file.readline().split()))
    file.close()

    a.sort()
    b.sort()

    total = sum(x * y for x, y in zip(a, b))
    print(total)

if __name__ == '__main__':
    main()
