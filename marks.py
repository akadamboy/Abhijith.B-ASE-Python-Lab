m1=int(input("enter mark1 out of 100"))
m2=int(input("enter mark2 out of 100"))
m3=int(input("enter mark3 out of 100"))
percent=((m1+m2+m3)/300)*100
if(percent>=90):
    print("grade : A")
elif(percent>=80):
    print("grade : B")
elif(percent>=70):
    print("grade : c")
elif(percent>=60):
    print("grade : d")
elif(percent>=50):
    print("grade : e")
else:
    ("failed")
    
