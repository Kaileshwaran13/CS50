sen = input("Text: ")
print(sen)


def countSen(sen):
    count = 0
    for i in sen:
        if i == "." or i == "?" or i == "!":
            count += 1

    return count


def countWords(sen):
    count = 0
    for i in sen:
        if i == " ":
            count += 1

    return count + 1


def countLetters(sen):
    count = 0
    for i in sen:
        if i.isalpha():
            count += 1

    return count


avgletter = float(countLetters(sen) / countWords(sen)) * 100
avgsen = float(countSen(sen) / countWords(sen)) * 100

grade = round(0.0588 * avgletter - 0.296 * avgsen - 15.8)

if grade < 1:
    print("Before Grade 1")
elif grade > 16:
    print("Grade 16+")
else:
    print(f"Grade {grade}")
