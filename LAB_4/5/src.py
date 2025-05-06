from tests import test_performance


def prefix_function(s):
    pi = [0]
    for i in range(1, len(s)):
        k = pi[i - 1]
        while k > 0 and s[i] != s[k]:
            k = pi[k - 1]
        if s[i] == s[k]:
            k += 1
        pi.append(k)
    return pi

@test_performance
def main():
    with open("test2.txt", "r") as file:
        s = file.readline().strip()
    pi = prefix_function(s)
    print(*pi)

if __name__ == '__main__':
    main()