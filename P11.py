import datetime
def grade(points):
    percentage = (points / 1000) * 100
    if points < 0:
        return "Points can't be negative"
    elif percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"
def main():
    start_time = datetime.datetime.now()
    print("Program started at:", start_time)
    point_file = open("points.txt", "r")
    grade_file = open("grades.txt", "w")
    error_file = open("error.txt", "w")
    records_read = 0
    records_written_grade = 0
    error_records = 0
    line = point_file.readline().strip()
    while line != "":
        records_read += 1
        parts = line.split(",")
        if len(parts) != 3:
            error_file.write(f"{line}, Incorrect format\n")
            error_records += 1
        else:
            id_number, name, points = parts
            try:
                points = int(points)
                if points < 0 or points > 1000:
                    error_file.write(f"{line}, Points must be between 0 and 1000\n")
                    error_records += 1
                else:
                    student_grade = grade(points)
                    grade_file.write(f"{id_number},{name},{points},{student_grade}\n")
                    records_written_grade += 1
            except ValueError:
                error_file.write(f"{line}, Points must be numeric\n")
                error_records += 1
        line = point_file.readline().strip()
    point_file.close()
    grade_file.close()
    error_file.close()
    print("Number of records read:", records_read)
    print("Number of records written to grade file:", records_written_grade)
    print("Number of error records:", error_records)
    end_time = datetime.datetime.now()
    print("Program ended at:", end_time)
main()
