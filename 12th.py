def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
text_in = input("Input  : ")
print(f"Output : {count_vowels(text_in)}")