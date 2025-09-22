marks=int(input("Enter Your Marks:"))
Grade="a"

if marks>=90 and marks<=100:
    grade='A'

elif marks<90 and marks>=75:
    grade='B'

elif marks<75 and marks>=60:
    grade='C'

elif marks<60 and marks>=50:
    grade='D'

elif marks<50:
    grade='F'

else :
    print(None)

print("Grade:",grade)