def Summation(data):
    Sum=0

    for i in data:
        Sum=Sum+i
    
    return Sum


def main():
    size =0
    Arr=list()

    print("Enter Number of Element :")
    size=int(input())

    print("Enter the Elements :")

    for i in range(size):
        no=int(input())
        Arr.append(no)

    ret=Summation(Arr)

    print("Summation : ",ret)


if __name__=="__main__":
    main()