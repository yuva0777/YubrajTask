grade=int(input("enter grade:"))
if grade>80:
    print("A")
elif grade>80 and grade>60:
    print("B")
elif grade>=50 and grade<60:
    print("C")
elif grade>=45 and grade<50:
    print("D")
elif grade>25 and grade<50:
    print("E")
else:
    print("F")