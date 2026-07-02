CheckEven=lambda No : (No%2==0)

def main():
    Value1=int(input("Enter Number :"))

    ret=CheckEven(Value1)   #ret=(No%2==0)
    if(ret==True):
        print("Its Even")
    else:
        print("Its Odd")
    

    
if __name__=="__main__":
    main()