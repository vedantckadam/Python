#Accept : Multiple parameter
#Return : One Value 

def Multiplication(no1,no2):
    return no1*no2

def Division(no1,no2):
    return no1/no2

def main():
    Ret1=Multiplication(11,21)
    print("Multication is : ",Ret1)

    Ret2=Division(12,6)
    print("Division is : ",Ret2)


if __name__=="__main__":
    main()