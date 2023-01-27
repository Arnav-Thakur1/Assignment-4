a=input("Enter the year(dd/mm/yyyy):")

b=int(a[6:10])
if b%4==0:
    if b%100==0:
        if b%400==0:
            print("The year is leap year")
        else:
            print("The year is not a leap year")
    else:
        print("The year is a leap year")
