num=int(input("enter the number"))
reverse=0

while (num>0):
    x=num%10
    reverse=reverse*10+x
    num=num//10
print("reverse number",reverse)
