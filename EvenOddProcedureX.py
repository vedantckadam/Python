def CheckEven(No1):
    bflag=False

    if (No1%2==0):
        bflag=True

    return bflag

def main():
    Value1=int(input("Enter Number :"))
    ret=CheckEven(Value1)
    print(ret)
    if(ret==True):
        print("Its Even")
    else:
        print("Its Odd")
    

    
if __name__=="__main__":
    main()
    
