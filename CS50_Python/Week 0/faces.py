def convert(sen):
    for i in  range(0,len(sen)):
        if sen[i] == "(" and sen[i - 1] == ":" or sen[i] == ")" and sen[i - 1] == ":":
           continue
        if sen[i] == ':' and sen[i + 1] == ')':
           print("🙂" , end = "")
        elif sen[i] == ':' and sen[i + 1] == '(':
           print("🙁" , end = "")
        else:
           print (sen[i],end = "")

def main():
    sen = input()
    convert(sen)

main()