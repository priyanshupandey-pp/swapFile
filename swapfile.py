def swapFilesData() :
    file1 = input("enter the first file")
    file2 = input("enter the second file")
    
    with open (file1,"r")  as a:
        data_a=a.read()
        
    with open (file2,"r")  as b:
        data_b=b.read()
        
    with open (file1,"w")  as a:
        data_a=a.write()
        
    with open (file2,"w")  as b:
        data_b=b.write()
swapFilesData()