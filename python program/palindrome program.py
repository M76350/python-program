i=int(input("enter the number"))
rev=0
x=i
while (i>0):
    rev=rev*10+i%10
    i=i//10
if rev==x:
    print("given number is palindrome number")
else:
     print("given number is palindrome number")
