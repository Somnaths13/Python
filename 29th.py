def find_longest_word(text):
    words = text.split()
    longest = ''
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
print(find_longest_word(input("Enter a sentence: ")))