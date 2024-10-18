m1=int(input("enter the mark 1"))
m2=int(input("enter the mark 2"))
m3=int(input("enter the mark 3"))
if(m1>m2 and m1>3):
    if(m2>m3):
       print("mark1 and mark2 is bigger")
       print("the avg of both is",(m1+m2)/2)
    else:
       print("mark1 and mark3 is bigger")
       print("the avg of both is",(m1+m3)/2) 
elif(m2>m1 and m2>3):
    if(m1> m3):
       print("mark2 and mark1 is bigger")
       print("the avg of both is",(m2+m1)/2) 
    else:
       print("mark2 and mark3 is bigger")
       print("the avg of both is",(m2+m3)/2)
else:
     if(m1>m2):
       print("mark3 and mark1 is bigger")
       print("the avg of both is",(m3+m1)/2) 
     else:
       print("mark3 and mark2 is bigger")
       print("the avg of both is",(m3+m2)/2)
