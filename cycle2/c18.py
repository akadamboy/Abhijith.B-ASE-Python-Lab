num=int(input("Enter the number:"))
flag=False
for i in range(2,num):
    if num%i==0:
        print(i)
        flag=True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
