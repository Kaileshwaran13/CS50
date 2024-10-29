sen = input("camelCase: ")

for i in range(0,len(sen)):
    if(sen[i] == sen[i].upper()):
        print(f"_{sen[i].lower()}",end = "")
    else:
        print(sen[i],end = "")