n=int(input("enter the number:"))
if(n%2==0):
    print("the number is even")
else:
    print("the number is odd")



num = int(input("Enter a number: "))
    
for i in range(2,num+1):
    for j in range(2,num+1):
        if i%j == 0:
            break
    if i == j:
        print(i,end=',')
