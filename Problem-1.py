class Calculator:
    def add(self, a, b):
        c= a+b
        print("Addition= ",c);
        
    def sub(self, a, b):
        c= a-b
        print("Substraction= ",c);
    
    def mul(self, a, b):
        c= a*b
        print("Multiplication= ",c);
    
    def div(self, a, b):
        c= a/b
        print("Division= ",c);

calcClass = Calculator()

while(True):
    a= float(input("Enter first number: "))
    b= float(input("Enter second number: "))
    operation= int(input("1. Addition\n2. Substraction\n3. Multiplication\n4. Division\nEnter choice: "))
    
    if operation== 1:
        calcClass.add(a,b)
    elif operation== 2:
        calcClass.sub(a,b)
    elif operation== 3:
        calcClass.mul(a,b)
    elif operation== 4:
        calcClass.div(a,b)
    else:
        print("Enter correct choice")
    
    continue1= input("Do you want to continue y or n\n")
    
    if(continue1=='n'):
        break