def Area( PI =3.14 ,Radius):    #Error (SyntaxError: parameter without a default follows parameter with a default)
    Ans=PI * Radius * Radius
    return Ans

def main():
    Ret =Area(12)
    print("Area of Circle is : ",Ret)

    Ret =Area(12,7.12)
    print("Area of Circle is : ",Ret)

if __name__=="__main__":
    main()
