TotalGrade = int(input("Please , Enter your total grade : "))
if (TotalGrade >= 0) and (TotalGrade<=100):
    if TotalGrade > 89:
     grade='A'
    elif TotalGrade >=79 :
     grade='B'
    elif TotalGrade > 69 :
     grade='C'
    elif TotalGrade > 59 :
     grade='D'
    else:
     grade='F'
    print("Your letter grade is : " , grade)
else:
    print("Please enter a grade between 0 and 100 ")


