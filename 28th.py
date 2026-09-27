def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    return result
text_in = input("Input:\n")
print("Output:")
print(remove_vowels(text_in))