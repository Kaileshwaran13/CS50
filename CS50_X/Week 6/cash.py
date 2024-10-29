num = input("Change: ")

while True:
    try:
        num = float(num)
        if num > 0:
            break
        else:
            num = input("Change: ")
    except ValueError:
        num = input("Change: ")


val = str(num).split(".")

if len(val[1]) == 1:
    val[1] = int(val[1]) * 10

num = int(val[0]) * 10**2 + int(val[1])

change = 0

while num > 0:
    if num >= 25:
        change += int(num / 25)
        num %= 25
    elif num >= 10:
        change += int(num / 10)
        num %= 10
    elif num >= 5:
        change += int(num / 5)
        num %= 5
    elif num >= 1:
        change += int(num / 1)
        num %= 1

print(change)
