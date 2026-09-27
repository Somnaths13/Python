def find_largest(a, b):
    if a > b:
        return a
    else:
        return b
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
print("Largest Number is:", find_largest(n1, n2))