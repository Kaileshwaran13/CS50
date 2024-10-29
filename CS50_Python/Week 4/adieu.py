import inflect

p = inflect.engine()
name_list = []

while True:
    try:
        name = input()
        if name != "":
            name_list.append(name)
        else:
            break
    except EOFError:
        break
output = p.join(name_list)
print("Adieu, adieu, to",output)