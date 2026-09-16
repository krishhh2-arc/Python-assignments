def calculate_grade(percentage):
    if percentage >= 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 60:
        return 'C'
    elif percentage >= 50:
        return 'D'
    else:
        return 'F'

def student_marks_analyzer():
    print("--- Student Marks Analyzer ---")
    
    try:
        num_subjects = int(input("Enter the total number of subjects: "))
        marks = []
        
        for i in range(1, num_subjects + 1):
            mark = float(input(f"Enter marks for Subject {i} (out of 100): "))
            marks.append(mark)
            
        total_marks = sum(marks)
        average_marks = total_marks / num_subjects
        percentage = (total_marks / (num_subjects * 100)) * 100
        grade = calculate_grade(percentage)
        
        print("\n--- Result Summary ---")
        print(f"Total Marks Obtained: {total_marks:.2f} / {num_subjects * 100}")
        print(f"Average Marks: {average_marks:.2f}")
        print(f"Percentage: {percentage:.2f}%")
        print(f"Grade: {grade}")
        print(f"Highest Marks: {max(marks)}")
        print(f"Lowest Marks: {min(marks)}")
        
    except ValueError:
        print("Invalid input. Please enter valid numerical values.")

if __name__ == "__main__":
    student_marks_analyzer()
  
