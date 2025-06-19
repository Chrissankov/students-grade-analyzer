number_students: int = int(input("Number of Students: "))  # O(1)
student_names = []  # O(1)
student_grades = []  # O(1)

# Overall complexity of the loop: O(n) where n = number of students
for student in range(number_students):  # O(n)
    student_name: str = input(str(student + 1) + " - Student Name: ")  # O(1)

    # In worst case, user keeps entering invalid grades m times: O(m)
    while True:  
        student_grade: int = int(input(str(student + 1) + " - Student Grade: "))  # O(1)
        if student_grade >= 0 and student_grade <= 100: # O(1) 
            break  # O(1)
        print("Grade must be between 0 and 100 inclusively.")  # O(1)

    student_names.append(student_name)  # O(1)
    student_grades.append(student_grade)  # O(1)

def display_student_name(): 
    for student in range(number_students):
        print("\n**** Student" , str(student + 1) , "****")
        print("Name:", student_names[student])
        print("Grade:", student_grades[student])

display_student_name()