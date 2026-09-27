def count_digits(n):
    n = abs(n)
    if n == 0:
        return 1
    count = 0
    while n > 0:
        count += 1
        n = n // 10
    return count
n = int(input("Enter a Number: "))
print(f"Total Digits = {count_digits(n)}")