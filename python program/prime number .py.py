num=eval(input("enter the num" ))



if num>=1:
    for i in range(2,num):
        if (num%i)==0:
            print("not prime number")
            break
    else:
        print("primary number")

else:
    print("not prime number")