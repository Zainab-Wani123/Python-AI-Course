#function for average marks
def average_marks(marks):
    sum_of_marks=sum(marks)
    number_of_subjects=len(marks)
    average_of_marks=sum_of_marks/number_of_subjects
    return average_of_marks
#calculate the grade  and return it
def calculate_grade(average):
    if average >= 80:
        return 'A'
    elif average >= 60:
        return 'B'
    elif average >= 50:
        return 'C'
    else:
        return 'F'

#function call
marks=[55, 64, 75, 80, 65]
avg=average_marks(marks)
#displaying the average marks
print("The average marks are:", avg)
#displaying the grade
grade=calculate_grade(avg)
print("The grade is:", grade)
# End of code
