s=input("Enter a string:")
a=s.split(" ")
b=[]
for i in a:
    if i not in b:
        b.append(i)
for i in b:
    print(i,"occures",a.count(i),"times")
