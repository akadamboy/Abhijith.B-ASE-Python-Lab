a=input("enter 1st set of colours seperated by comas :")
b=input("enter thge 2nd set of colours seperated by comas :")
a=a.split(',')
b=b.split(',')
s1=set(a)
s2=set(b)
print(s1)
print(s2)

print("difference of set1, set2 is :",s1.difference(s2))
