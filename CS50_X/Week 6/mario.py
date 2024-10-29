num = input("Height: ")

while(True):
    if(num.isdigit() == True and int(num) >= 1 and int(num) <= 8):
        break
    else:
        num = input("Height: ")

num = int(num)
for i in range(1,num+1):
    for j in range(0,num-i):
        print(" ",end = "")
    for j in range(0,i):
        print("#",end = "")
    print()
