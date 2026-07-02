def filterX(Task,Elements):
    Result=[]
    for no in Elements:
        ret=Task(no)    #CheckEven(No)
        if ret==True:
            Result.append(no)
    
    return Result

def mapX(Task,Elemets):
    Result=[]

    for no in Elemets:
        ret=Task(no)
        Result.append(no)
    
    return Result

def reduceX(Task , Elements):
    Sum=0

    for no in Elements:
        Sum=Task(Sum,no)

    return Sum


