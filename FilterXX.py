def main():
    Data=[13,12,8,10,11,20]

    CheckEven=lambda No :(No%2==0)
    
    print("Input Data is : ",Data)

    fData=list(filter(CheckEven,Data))

    print("Data After Filter : ",fData)



if __name__=="__main__":
    main()