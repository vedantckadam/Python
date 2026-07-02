def main():
    Marks=[78,89,99,65,44]

    for no in Marks:
        print(no)
    
    Marks[2]=98

    print("-"*25)
    print("After updation")
    print("-"*25)
    for no in Marks:
        print(no)



if __name__=="__main__":
    main()