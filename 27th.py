def display_position(text):
    for i in range(len(text)):
        print(f"Position {i} : {text[i]}")
text_in = input("Input:\n")
print("Output:")
display_position(text_in)