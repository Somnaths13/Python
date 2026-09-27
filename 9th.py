def reverse_number(n):
    result = 1
    s = 0
    while n > 0:
        result = n % 10
        s = s*10 + result
        n = n // 10
    return s
number = int(input("Enter a number: "))
print(reverse_number(number))