def check_palindrome(text):
    text = text.lower()
    if text == text[::-1]:
        print(f"{text} :  Palindrome")
    else:
        print(f"{text} :  Not Palindrome")
check_palindrome(input("Enter a string: "))