print("Amount Due: 50")
coin = 1
due = int(50)
while(coin > 0):
    coin = int(input("Insert Coin: "))
    if(coin == 25 or coin == 10 or coin == 5):
        due = due - coin
    if(due == 0):
        print("Change Owed:" , abs(due))
        break
    else:
        if(due < 0):
            print("Change Owed:", abs(due))
            break
        else:
            print("Amount Due:",abs(due))
