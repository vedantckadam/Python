def BigBazar():
    print("Inside BigBazar")

    def Amul():
        print("Inside Amul IceCreame Palour") 
    

def main():
    BigBazar()       #Alowed
    Amul()           #Error   
    BigBazar.Amul()  #Error (AttributeError: 'function' object has no attribute 'Amul')

if __name__=="__main__":
    main()