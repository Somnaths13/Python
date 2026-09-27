def count_vowels_consonants(text):
    vowels = "aeiouAEIOU"
    v_count = 0
    c_count = 0
    for char in text:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
    print(f"Vowels     : {v_count}")
    print(f"Consonants : {c_count}")
text_in = input("Input : ")
count_vowels_consonants(text_in)