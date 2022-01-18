def factorial(num):
    n=1
    for i in range(1,num+1):
        n=n*i
    return n
num =int(input("Enter the number:"))
print("Factorial of",num,"is",factorial(num))
