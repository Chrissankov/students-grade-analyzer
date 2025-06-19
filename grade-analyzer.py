number_students: int = int(input("Number of Students: ")) # O(1)
student_names = [] # O(1)
student_grades = [] # O(1)

# Overall complexity of the loop: O(n)
for student in range(number_students): # O(1)
    student_name: str = input(str(student + 1) + " - Student Name: ") # O(1)

    # In worst case user keeps entering invalid grades m times: O(m)
    while True:  
        student_grade: int = int(input(str(student + 1) + " - Student Grade: ")) # O(1)
        if student_grade >= 0 and student_grade <= 100: # O(1) 
            break # O(1)
        print("Grade must be between 0 and 100 inclusively.") # O(1)

    student_names.append(student_name) # O(1)
    student_grades.append(student_grade) # O(1)

# Overall complexity of the function: O(n) 
def display_student_name(): # O(1)
    for student in range(number_students): # O(n)
        print("\n**** Student" , str(student + 1) , "****") # O(1)
        print("Name:", student_names[student]) # O(1)
        print("Grade:", student_grades[student]) # O(1)

# Calling the function
display_student_name() # O(1)

# Overall complexity of the function: O(n) 
def get_avg_grade(grades, count_students): # O(1)
    sum = 0 # O(1)
    for student_grade in grades: # O(n)
        sum += student_grade # O(1)
    print("\nAverage Grade of the Class:", sum / count_students ) # O(1)

# Calling the function
get_avg_grade(student_grades, number_students) # O(1)

# Overall complexity of the function: O(n) 
def get_highest_grade(grades, names, index=0, max_index=0): # O(1)
    if index == len(grades): # O(1)
        print("\n**** Highest Grade ****") # O(1)
        print("Name:", names[max_index]) # O(1)
        print("Grade:", grades[max_index]) # O(1)
        return # O(1)
    
    if grades[index] > grades[max_index]: # O(1)
        max_index = index # O(1)

    return get_highest_grade(grades, names, index + 1, max_index) # O(n)

# Calling the function
get_highest_grade(student_grades, student_names)