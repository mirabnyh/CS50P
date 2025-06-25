phrase = input("Input: ")
for c in phrase:
    if c.lower() in ['a', 'e', 'i', 'u', 'o']:
        phrase = phrase.replace(c, '')

print(f"Output: {phrase}")
