def check_even_odd(n):
    if n % 2 == 0:
        print(f"{n} is Even Number")
    else:
        print(f"{n} is Odd Number")

print('Even or Odd')
check_even_odd(int(input("Enter a Number: ")))