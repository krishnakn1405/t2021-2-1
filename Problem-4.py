while(True):
    list1= [1,2,3,4,5,6,7,8,9]
    list2= []
    dictionary1={}
    
    total= int(input("Enter number of elements in list: "))
    
    for i in range(0, total):
        elem = int(input())
        list2.append(elem)  
    
    len_list2= len(list2)
    
    for i in list1:
        k=0
        l=0
        for j in list2:
            l=l+1
            if j%i==0:
                k=k+1
            if(l==len_list2):
                dictionary1[i] = k
            
    print(dictionary1)
    
    continue1= input("Do you want to continue y or n\n")
    
    if(continue1=='n'):
        break