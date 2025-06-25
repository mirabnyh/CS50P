phrase = input("camelCase: ")
for char in phrase:
    if char.isupper():
        phrase = phrase.replace(char, f"_{char}")
print(phrase.lower())
