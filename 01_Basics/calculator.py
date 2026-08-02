a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
op=input("Enter operator (+, -, *, /, %, **, //): ")
if(op=="+"):
    print("Addition:", a + b)
elif(op=="-"):
    print("Subtraction:", a - b)
elif(op=="*"):
    print("Multiplication:", a * b)
elif(op=="/"):
    print("Division:", a / b)
elif(op=="%"):
    print("Modulus:", a % b)
elif(op=="**"):
    print("Exponent:", a ** b)
elif(op=="//"):
    print("Floor Division:", a // b)
else:
    print("Invalid operator. Please use one of the following: +, -, *, /, %, **, //")