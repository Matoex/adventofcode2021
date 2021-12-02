with open("input.csv", "r") as file:

    values = file.read()
    values = values.split("\n")
    
    counter = 0

    a=None
    b=None
    c=None
    for x in values:
        x=int(x)
        if a != None and b != None and c != None:
            
            s1=a+b+c
            s2=b+c+x

            if s2>s1:
                counter+=1
        a=b
        b=c
        c=x
                
    print counter