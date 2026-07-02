import Marvellous as VK

def main():
    
    print("Enter First Number :")
    Value1=int(input())

    print("Enter Second Number :")
    Value2=int(input())

    ret=VK.Addition(Value1,Value2) 

    print("Addition of Numbers are : ",ret)

if __name__=="__main__":
    main()
