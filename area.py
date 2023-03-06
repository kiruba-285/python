#to find the grade and avg mark of the student
mark=100
M1=float(input("enter the mark of a student 1:"))
M2=float(input("enter the mark of a student 2:"))
M3=float(input("enter the mark of a student 3:"))
M4=float(input("enter the mark of a student 4:"))
M5=float(input("enter the mark of a student 5:"))
avg=(M1+M2+M3+M4+M5)/5
print("The average mark of a student:",avg )
if(M1==mark):
    print("this is the topper")
elif(M2<=mark):
    print(" not the topper")
elif(M3<=mark):
    print("not the topper")   
elif(M4<=mark):
    print("not the topper")
elif(M5<=mark):
    print("not the topper")

    
    
