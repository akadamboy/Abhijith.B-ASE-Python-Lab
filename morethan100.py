a=input("enter a list of numbers  : ")
l=a.split(" ")
b=list(map(int,l))
for  i in range(len(b)):
    if(b[i]>100):
        l[i]='over'
print(l)
