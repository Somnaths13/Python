def count_each_vowel(text):
    count_a = 0
    count_e = 0
    count_i = 0
    count_o = 0
    count_u = 0

    for char in text.lower():
        if char == 'a':
            count_a += 1
        elif char == 'e':
            count_e += 1
        elif char == 'i':
            count_i += 1
        elif char == 'o':
            count_o += 1
        elif char == 'u':
            count_u += 1

    print(f"a = {count_a}")
    print(f"e = {count_e}")
    print(f"i = {count_i}")
    print(f"o = {count_o}")
    print(f"u = {count_u}")
text_in = input("Input:\n")
print("Output:")
count_each_vowel(text_in)