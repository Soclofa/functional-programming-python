# Importing the necessary module
import Targil4input

# Function to process and calculate statistics for each teacher
def myStudList(teachers, students): 
    if not teachers or not students: 
        return [], 0, 0

    def stats_functions(lst):
        def average():
            return sum(lst) / len(lst) if lst else 0

        def stdDev():
            avg = average()
            variance = sum((x - avg) ** 2 for x in lst) / len(lst) if lst else 0
            return variance ** 0.5

        return average(), stdDev()

    processed_teachers = [
        [
            teacher[0], 
            [student[0] for student in students if student[2] == teacher[1]], 
            stats_functions([student[1] for student in students if student[2] == teacher[1]])
        ]
        for teacher in teachers
    ]

    all_grades = [student[1] for student in students]
    overall_avg, overall_stddev = stats_functions(all_grades)

    return processed_teachers, overall_avg, overall_stddev

# Function to convert the processed list to a dictionary
def myStudDict(L):
    return {item[0]: (item[1], item[2]) for item in L}

# Helper function to format a single teacher's data
def format_teacher_data(teacher_data):
    teacher, (student_ids, (avg, stddev)) = teacher_data
    return f"Teacher: {teacher}, Student IDs: {student_ids}, Average: {avg:.2f}, StdDev: {stddev:.2f}"

# Main function to execute the program without an explicit for loop
def main():
    # Get the processed list of teachers and statistics
    teachers, avg_all, stddev_all = myStudList(Targil4input.teacherName, Targil4input.jctMarks)
    
    # Convert the list to a dictionary
    teacher_dict = myStudDict(teachers)
    
    # Format the teacher data without an explicit for loop
    formatted_teacher_data = map(format_teacher_data, teacher_dict.items())
    
    # Print the formatted teacher data
    print("\n".join(formatted_teacher_data))
    
    # Print the overall statistics
    print(f"Overall Average: {avg_all:.2f}, Overall StdDev: {stddev_all:.2f}")

if __name__ == "__main__":
    main()
