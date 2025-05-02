n = 10**5

with open("deep_tree.txt", "w") as f:
    f.write(f"{n}\n")
    for i in range(n - 1):
        f.write(f"{i} {i+1} -1\n")
    f.write(f"{n - 1} -1 -1\n")