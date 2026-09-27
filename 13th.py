def count_consonants(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char.isalpha() and char not in vowels:
            count += 1
    return count
text_in = input("Enter a string: ")
print(f"Consonants Count = {count_consonants(text_in)}")