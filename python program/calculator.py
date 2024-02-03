num1=int(input("enter a first number "))

operator =input("chose operator (+,-,*,/,%)")

num2=int(input("enter second number"))

if operator =="+":
	print('sum of' ,num1,'and',num2, 'is = ',num1+num2)
	
elif operator =="-":
	print('subtract of',num1,'and',num2,'is = ',num1-num2)
	
elif operator =="*":
	print('miltiply of ',num1,'and',num2,'is = ',num1*num2)
	
elif operator =="/":
	print('divison of ',num1, 'and',num2,'is = ',num1/num2)
	
elif operator =="%":
	print('remendar of ',num1,'and',num2,'is =',num1%num2)
else:
	print("invalid operator ")												