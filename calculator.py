def calci():
    num1=int(input("enter the 1st num"))
    num2=int(input("enter the 2nd num"))
    print("Choose operation (+,-,*,/) to perform calculation and q to stop")
    opt=0
    while opt!="q":
        opt=input("Enter the operation")
        if opt=="+":
            print("sum=", num1+num2)
        elif opt=="-":
            print("sub=",num1-num2)
        elif opt=="*":
            print("prod=", num1*num2)
        elif opt=="/":
            print("division=", num1/num2)
    print(" End")
calci()
        
    
