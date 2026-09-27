def character_frequency(text, ch):
    freq = 0
    for char in text:
        if char == ch:
            freq += 1
    return freq
text_in = input("Text      : ")
char_in = input("Character : ")
print(f"Frequency : {character_frequency(text_in, char_in)}")