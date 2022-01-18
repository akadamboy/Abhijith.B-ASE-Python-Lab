a=int(input("Enter the number:"))
print("Factors of number",a,"are:")
for i in range(1,a+1):
    if a%i==0:
        print(i)
        
