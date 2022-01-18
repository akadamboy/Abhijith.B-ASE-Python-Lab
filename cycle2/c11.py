s=input("Enter the integers:")
k=map(int,s.split(" "))
l=list(k)
j=[x for x in l if x>0]
print(j)
