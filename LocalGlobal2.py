no=11 #global variable

def Display():
    a=21        #local variable
    print("from display value of a is :",a)     
    print("from Diaply :",no)

def Demo():
    print("from demo value of a is :",a)     #Error(NameError: name 'a' is not defined)
    print("from Demo :",no)

Display()
Demo()