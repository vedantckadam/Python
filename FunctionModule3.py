from Marvellous import Addition

def main():
    
    print("Enter First Number :")
    Value1=int(input())

    print("Enter Second Number :")
    Value2=int(input())

    ret=Addition(Value1,Value2) 
    ret1=Subtraction(Value1,Value2)     #Error (NameError: name 'Subtraction' is not defined)

    print("Addition of Numbers are : ",ret)

    print("Subtraction of Numbers are : ",ret1)

if __name__=="__main__":
    main()
