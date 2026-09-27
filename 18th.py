def count_words(text):
    count = 1
    for ch in text:
        if ch == ' ':
            count += 1
    return f"Number of words are {count}"
print(count_words(input("Enter a Sentence: ")))