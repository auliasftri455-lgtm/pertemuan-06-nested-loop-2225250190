n = int(input("n: "))
banyak = 0

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        print(f"({i}, {j})")
        banyak += 1

print(f"Banyak pasangan = {banyak}")