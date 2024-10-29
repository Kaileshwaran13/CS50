import random

def main():
    level = get_level()
    if level:
        score = generate_integer(level)
        print(f"{score}")

def get_level():
    while True:
        level = input("Level: ")
        if level.isdigit() and level in ["1", "2", "3"]:
            return int(level)
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

def generate_integer(level):
    score = 0
    for _ in range(10):
        num1, num2 = generate_numbers(level)
        loss = 3
        while loss > 0:
            answer = input(f"{num1} + {num2} = ")
            if answer.isdigit() and int(answer) == num1 + num2:
                score += 1
                break
            else:
                print("EEE")
                loss -= 1
        else:
            print(f"{num1} + {num2} = {num1 + num2}")
    return score

def generate_numbers(level):
    if level == 1:
        return random.randint(0, 9), random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99), random.randint(10, 99)
    else:
        return random.randint(100, 999), random.randint(100, 999)

if __name__ == "__main__":
    main()