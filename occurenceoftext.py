a=input("enter a string : ")
a=a.split(" ")
b=[]
for i in a:
    if i not in b:
        b.append(i)
for i in b:
    print(i,"occure ",a.count(i)," times")
    
    
       
