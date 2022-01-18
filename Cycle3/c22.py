n=int(input("Enter the number:"))
a=0
b=1
print(a)
for i in range(2,n+1):
    print(b)
    c=b
    b=a+b
    a=c

