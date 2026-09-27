def count_characters(text):
    count = 0
    for _ in text:
        count += 1
    return count
text_in = input("Enter a string: ")
print(f"Total Characters = {count_characters(text_in)}")