#Accept : Multiple parameter
#Return : One Value 

def Calculation(no1,no2):
    Multi=no1*no2
    Div=no1/no2

    return Multi,Div

def main():
    
    Value1=int(input("Enter First Number :"))
    Value2=int(input("Enter Second Number :"))

    ret1,ret2=Calculation(Value1,Value2)

    print("Multiplication is : ",ret1)
    print("Division is : ",ret2)

    

if __name__=="__main__":
    main()