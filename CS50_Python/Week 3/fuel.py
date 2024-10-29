import math
while True:
    string = input("Fraction: ")
    symbol = string.find("/")
    try:
        x = int(string[:symbol])
        y = int(string[symbol + 1:])
        percent = int( round(( x / y ) * 100) )
        if(x > y):
            continue
        break
    except (ValueError , ZeroDivisionError):
        continue
if(percent > 90):
    print("F")
elif(percent < 10):
    print("E")
else:
    print(str(percent)+"%")