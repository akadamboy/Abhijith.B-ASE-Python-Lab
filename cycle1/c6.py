l=input("Enter thel ist")
l1=map(int,l.split(" "))
s=list(l1)
l2=[x for x in s if x%2!=0]
print("After removing even number the list is:",l2)
   
        
