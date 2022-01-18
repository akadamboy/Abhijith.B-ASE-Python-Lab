a=int(input("enter the first number : "))
b=int(input("enter the second number:  "))
gcd=0
if(a<b):
    small=a
else:
    small=b
for i in range(1,small+1):
    if((a%i==0) and (b%i==0)):
        gcd=i
print("gcd of ",a," and ",b," is ",gcd)
