a=int(input("Enter the marks: "))
if a<100:
    print("Grade:")
    if a<25:
        print("F")
    if 25<=a<45:
        print("E")
    if 45<=a<50:
        print("D")
    if 50<=a<60:
        print("C")
    if 60<=a<80:
        print("B")
    if 80<=a<100:
        print("A")
else:
    print('Enter marks between 0 to 100')