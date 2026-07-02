def Summation(Data):
    Sum=0
    for no in range(len(Data)):
        Sum=Sum+Data[no]
    
    print("Summation of Marks : ",Sum)
    

def main():
    Marks=[78,89,99,65,44]
    iRet=Summation(Marks)
    
if __name__=="__main__":
    main()