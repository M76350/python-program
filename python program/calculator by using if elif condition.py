a=int(input("enter the first num"))
operation=input("enter the operation(+,-,*,%)")
b=int(input("enter the second  num"))

if operation=="+":
    print(a+b)
elif operation=="-":
    print(a-b)
elif operation=="*":
    print(a*b)
elif operation=="%":
    print(a%b)
elif operation == "/":
    print(a / b)
else:
    print("invalid operation")
