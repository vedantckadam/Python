def main():
    Marks=[78,89,99,65,44]
    Sum=0

    for no in range(len(Marks)):
        Sum=Sum+Marks[no]
    
    print("Summation of Marks : ",Sum)


if __name__=="__main__":
    main()