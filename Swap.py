def SwapData():
    name1=input("Enter the name of 1st file: ")
    name2=input("Enter the name of 2nd file: ")

    with open(name1,'r') as a:
        data_a=a.read()

    with open(name2,'r') as b:
        data_b=b.read()

    with open(name1,'w') as a:
        a.write(data_b)
    with open(name2,'w') as b:
        b.write(data_a)
    
    

SwapData()