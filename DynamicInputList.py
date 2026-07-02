def main():
    size =0
    Arr=list()

    print("Enter Number of Element :")
    size=int(input())

    print("Enter the Elements :")

    for i in range(size):
        no=int(input())
        Arr.append(no)

    print(Arr)



if __name__=="__main__":
    main()