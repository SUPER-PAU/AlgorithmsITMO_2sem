from random import randint
from tests import test_performance

def compute_hashes(s, x, m):
    n = len(s)
    h = [0] * (n + 1)
    x_pows = [1] * (n + 1)
    for i in range(1, n + 1):
        h[i] = (x * h[i - 1] + ord(s[i - 1])) % m
        x_pows[i] = (x_pows[i - 1] * x) % m
    return h, x_pows

def substring_hash(h, x_pows, a, l, m):
    # h[a + l] - x^l * h[a] mod m
    return (h[a + l] - x_pows[l] * h[a] % m + m) % m

@test_performance
def main():
    commands = []
    with open("test.txt", "r") as file:
        s = file.readline().strip()
        q = int(file.readline())
        for _ in range(q):
            commands.append(tuple(map(int, file.readline().split())))

    x = randint(1, 10**9)
    m1 = 10**9 + 7
    m2 = 10**9 + 9

    h1, x1_pows = compute_hashes(s, x, m1)
    h2, x2_pows = compute_hashes(s, x, m2)
    # print(h1, x1_pows)
    # print(h2, x2_pows)

    for a, b, l in commands:
        h1_a = substring_hash(h1, x1_pows, a, l, m1)
        h1_b = substring_hash(h1, x1_pows, b, l, m1)
        h2_a = substring_hash(h2, x2_pows, a, l, m2)
        h2_b = substring_hash(h2, x2_pows, b, l, m2)

        if h1_a == h1_b and h2_a == h2_b:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()
