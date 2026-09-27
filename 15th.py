def reverse_string(text):
    reverse = ''
    for i in text:
        reverse = i + reverse
    return f"Reverse of this string: {reverse}"
print(reverse_string(input("Enter a string: ")))