def convert_uppercase(text):
    word = ' '
    for ch in text:
        word = word + ch.upper() 
    return word
print(convert_uppercase(input('Enter a string: ')))