import random


def main():
    score = 0
    level = get_level()
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        equation = int(input(f"{x} + {y} = "))
        if equation == x + y:
            score += 1
            continue
        print("EEE")
        for i in range(2):
            equation = int(input(f"{x} + {y} = "))
            if equation != x+y:
                print("EEE")
            else:
                score += 1
                break
        print((f"{x} + {y} = {x+y}"))
    print(score)

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n not in [1, 2, 3]:
                continue
            return n
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    return random.randint(100,999)


if __name__ == "__main__":
    main()
