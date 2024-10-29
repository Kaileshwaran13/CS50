menu = {
    "baja taco": 4.00,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}
total = 0
while True:
    try:
        order = input("Item: ")
        try:
            order = order.lower()
            if(order == ""):
                break
            total = total + menu[order]
            print("$"+str(format(total,".2f")))
        except KeyError:
            continue
    except EOFError:
        print()
        break