from tests import test_performance


@test_performance
def main():
    with open('test2.txt', 'r', encoding='utf-8') as file:
        n = int(file.readline())
        lectures = []
        for _ in range(n):
            s, f = map(int, file.readline().split())
            lectures.append((s, f))
    file.close()

    lectures.sort(key=lambda x: x[1])

    count = 0
    current_end = 0

    for start, end in lectures:
        if start >= current_end:
            count += 1
            current_end = end

    print(count)

if __name__ == '__main__':
    main()
