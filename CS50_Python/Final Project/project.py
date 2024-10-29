def main():
        sen = (input("Enter a equation: "))
        try:
            sen = sen.split(" ")
            match(sen[1]):
                case '+':
                    print(add(sen[0],sen[2]))
                case '-':
                    print(sub(sen[0],sen[2]))
                case '*':
                    print(mul(sen[0],sen[2]))
                case '/':
                    print(div(sen[0],sen[2]))
                case _:
                    return None
        except(IndexError,ValueError):
                print("Give the data in this format (num1 operator num2) ans check the given datas are numbers")
                main()

def add(a,b):
    return(float(a) + float(b))

def sub(a,b):
    return(float(a) - float(b))

def mul(a,b):
    return(float(a) * float(b))

def div(a,b):
    return(float(a) / float(b))

if __name__ == "__main__":
    main()
