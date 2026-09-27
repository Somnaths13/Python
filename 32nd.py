def number_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()
n_in = int(input("Enter n: "))
number_pattern(n_in)