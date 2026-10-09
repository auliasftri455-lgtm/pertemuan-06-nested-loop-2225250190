n = int(input("n: "))

for i in range(1, n + 1):
    jumlah = 0

    for j in range(1, n + 1):
        hasil = i * j
        print(f"{hasil:4}", end="")
        jumlah += hasil

    print(f" | jumlah = {jumlah}")