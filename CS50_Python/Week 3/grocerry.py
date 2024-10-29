grocerry = []
while True:
    try:
        item = input()
        if(item == ""):
            break
        grocerry.append(item.upper())
    except EOFError:
        print()
        break
grocerry.sort()


list = {}
for i in grocerry:
    list[i] = grocerry.count(i)

for i in list:
    print(list[i],i)