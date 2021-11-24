a=input("enter 1st list of numbers seperated by comas : ")
a=a.split(",")
a=list(map(int,a))
c=[x for x in a if x%2!=0]
print(c)
