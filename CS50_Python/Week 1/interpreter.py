ans = input("Expression: ")
ans = ans.split(" ")
x = float(ans[0])
y = ans[1]
z = float(ans[2])
if(y == '+'):
    print(x+z)
elif(y == '-'):
    print(x-z)
elif(y == '*'):
    print(x*z)
else:
    print(x/z)