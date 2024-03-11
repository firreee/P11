import datetime

def calculate_grade(points):
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

    with open("points.txt", "r") as infile:
        with open("grades.txt", "w") as grade_file, open("error.txt", "w") as error_file:
            records_read = 0
            grade_file = 0
            error_records = 0
            
            line = infile.readline().strip()
            
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
                            grade = calculate_grade(points)
                            grade_file.write(f"{line},{grade}\n")
                            grade_file += 1
                    except ValueError:
                        error_file.write(f"{line}, Points must be numeric\n")
                        error_records += 1

                line = infile.readline().strip()

    print("Number of records read:", records_read)
    print("Number of records written to grade file:", grade_file)
    print("Number of error records:", error_records)
    
    end_time = datetime.datetime.now()
    print("Program ended at:", end_time)
main()
