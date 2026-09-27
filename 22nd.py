def count_case(text):
    upper_count = 0
    lower_count = 0
    digit_count = 0
    space_count = 0
    
    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char == ' ':
            space_count += 1

    print(f"Uppercase : {upper_count}")
    print(f"Lowercase : {lower_count}")
    print(f"Digits    : {digit_count}")
    print(f"Spaces    : {space_count}")
text_in = input("Input: ")
count_case(text_in)