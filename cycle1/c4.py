li=input("Enter a list of numbers")
l=list(map(int,li.split(" ")))
for i in range(len(l)):
    if l[i]>=100:
        l[i]='over'
print(l)
