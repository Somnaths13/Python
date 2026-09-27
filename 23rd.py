def first_character(text):
    for char in text:
        print(f"First character: {char}")
        break
text_in = input("Enter a string: ")
first_character(text_in)