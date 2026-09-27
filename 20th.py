def remove_spaces(text):
    result = ""
    for char in text:
        if char != " ":
            result += char
    return result
text_in = input("Input  : ")
print(f"Output : {remove_spaces(text_in)}")