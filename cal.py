x = int(input("enter number :"))
y = int(input("Enter second number :"))
z = (input("Enter the operation :") )

if (z == '+'):
    res = x + y 
elif (z == '-'):
    res = x - y    
elif (z == '*'):
    res = x * y 
elif (z == '/'):
    res = x / y 
elif (z == '%'):
    res = x % y 
else:
    print("invalid input !")

print(res)