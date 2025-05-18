def get_grade_point(grade):
    

    grade = grade.upper()  # Convert to uppercase for consistent comparison
    if grade == 'A':
        return 4.0
    elif grade == 'B':
        return 3.0
    elif grade == 'C':
        return 2.0
    elif grade == 'D':
        return 1.0
    elif grade == 'F':
        return 0.0
    else:
        return -1  # Indicate an invalid grade

def calculate_gpa(num_courses=6):
    total_quality_points = 0
    total_credit_hours = 0
    
    print("\n--- GPA Calculator for 6 Courses ---")
    print("Enter grades (A, B, C, D, F) and credit hours for each course.")
    print("Invalid grades will result in an error.\n")

    for i in range(1, num_courses + 1):
        while True:
            try:
                print(f"--- Course {i} ---")
                grade = input(f"Enter grade for Course {i} (e.g., A, B, C, D, F): ").strip()
                grade_point = get_grade_point(grade)

                if grade_point == -1:
                    print("Invalid grade entered. Please use A, B, C, D, or F.")
                    continue # Ask for grade again
                
                credit_hours = float(input(f"Enter credit hours for Course {i}: ").strip())
                
                if credit_hours <= 0:
                    print("Credit hours must be a positive number. Please try again.")
                    continue # Ask for credit hours again
                
                # If both grade and credit hours are valid, break the inner loop
                break 
            except ValueError:
                print("Invalid input for credit hours. Please enter a number.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

        quality_points = grade_point * credit_hours
        total_quality_points += quality_points
        total_credit_hours += credit_hours

    if total_credit_hours == 0:
        print("\nNo credit hours entered. Cannot calculate GPA.")
        return 0.0
    else:
        gpa = total_quality_points / total_credit_hours
        print(f"\n--- GPA Calculation Results ---")
        print(f"Total Quality Points: {total_quality_points:.2f}")
        print(f"Total Credit Hours: {total_credit_hours:.2f}")
        print(f"Your GPA for {num_courses} courses is: {gpa:.2f}")
        return gpa

if __name__ == "__main__":
    calculate_gpa(num_courses=6)