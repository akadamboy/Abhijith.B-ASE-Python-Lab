a=input("enter a list of numbers seperated by comas : ")
a=a.split(",")
a=list(map(int, a))
print(type(a[1]))
for i in range(0,len(a)):
    if a[i]>100:
        a[i]="over"
print(a)
