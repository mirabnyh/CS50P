def main():
    word = input("Input: ")
    print(shorten(word))


def shorten(phrase):
    for c in phrase:
    if c.lower() in ['a', 'e', 'i', 'u', 'o']:
        phrase = phrase.replace(c, '')

    return (f"Output: {phrase}")

if __name__ == "__main__":
    main()
