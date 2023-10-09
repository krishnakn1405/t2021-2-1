while(True):
    a= int(input("Enter number to generate series: "))
    
    for i in range(a):
        if i==0:
            b= 1
        else:
            b=b+2
        print(b)
    
    continue1= input("Do you want to continue y or n\n")
    
    if(continue1=='n'):
        break