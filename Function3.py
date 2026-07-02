def main():
    print("Enter First Number :")
    Value1=int(input())

    print("Enter Second Number :")
    Value2=int(input())

    ret=Addition(Value1,Value2)     #Error in this (NameError: name 'Addition' is not defined)

    print("Addition of Numbers are : ",ret)

if __name__=="__main__":
    main()
