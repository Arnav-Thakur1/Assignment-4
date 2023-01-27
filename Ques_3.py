import random

i=1
while i<=10:
    n1=random.randint(0,9)
    n2=random.randint(0,9)

    print(n1,'*',n2,'=')
    Answer=int(input('Enter the answer\n'))

    if Answer==n1*n2:
        print("Right!")
    else: 
        print("Wrong. The answer is", n1*n2)
    
    i=i+1
