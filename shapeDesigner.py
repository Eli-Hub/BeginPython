def gh (y,z):
    b=0
    for y in range (0,y):
        b+=1
        print (z * b)
        c=b
    while c>=(y-c)-y:
        c-=1
        print (z*c)
    print ("No. of Columns: ", (y*2)+1)
    
col = int (input("Enter No. of Columns before decrease: "))
shape=input ("Enter the Symbol to use for shape: ")
gh(col,shape)