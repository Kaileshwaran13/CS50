greetings = input("Greeting: ")

greetings = greetings.strip()

if(greetings[0] == 'H' or greetings[0] == 'h'):
    greetings = greetings.replace(","," ")
    greetings = greetings.split(" ")
    if(greetings[0].strip() == "Hello" or greetings[0].strip() == "hello"):
        print("$0")
    else:
        print("$20")
else:
    print("$100")