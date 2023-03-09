CH=int(input("no of classes held: "))
CA=int(input("no of classes attended:"))
attendance=(CA)/(CH) *100
print("attendance= ",attendance)
if attendance<75:
    print("The student is not eligible to attend the sem exam")
else:
    print("The student is eligible to attend the sem exam")
