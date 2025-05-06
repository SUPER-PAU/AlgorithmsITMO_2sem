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
    print(pi)
    return pi

def kmp(p, t):
    s = p + "#" + t
    pi = prefix_function(s)
    result = []
    len_p = len(p)
    len_s = len(s)
    for i in range(len_p + 1, len_s):
        print(s[i])
        if pi[i] == len_p:
            result.append(i - (len_p + 2))
    return result


@test_performance
def main():
    with open("test1.txt", 'r') as file:
        p = file.readline().strip()
        t = file.readline().strip()

    res = kmp(p, t)
    print(len(res))
    print(res)

if __name__ == "__main__":
    main()
    