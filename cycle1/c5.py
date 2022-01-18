l1=input("Enter 1st list")
l1l=map(int,l1.split(" "))
l1l1=list(l1l)
l2=input("Enter 2st list")
l2l=map(int,l2.split(" "))
l2l2=list(l2l)
a=len(l1l1)
b=len(l2l2)
if a==b:
    print("Both list are equal")
else:
    print("Lists are not equal")
for x in l1l1:
    s1=sum(l1l1)
for x in l2l2:
    s2=sum(l2l2)
if s1==s2:
    print("Sum of both lists are equal")
else:
    print("Sum of both lists are not equal")
p=set(l1l1)
q=set(l2l2)
for x in p:
    for i in q:
        s3=p.intersection(q)
print("Values occures in both:",list(s3))
