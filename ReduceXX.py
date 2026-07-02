from functools import reduce

CheckEven = lambda No:(No%2==0)
    

Increment =lambda No:No+1  

Addition=lambda No1 , No2 :No1+No2
    
def main():
    Data=[13,12,8,10,11,20]

    print("Input Data is : ",Data)

    fData=list(filter(CheckEven,Data))

    print("Data After Filter : ",fData)

    mData=list(map(Increment,fData))

    print("Data After Map : ",mData)

    rData=list(reduce(Addition,mData))

    print("Data After Reduce : ",rData)

if __name__=="__main__":
    main()