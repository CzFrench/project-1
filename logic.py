import csv
import os


def grade_scale(score: float) -> str:
    """
    This functions is a grade scale, it grabs the numeric score and determines a letter grade.
    :param score: This is a students grade represented by a FLOAT.
    :return grade: Returns letter grade represented by a STRING.
    """
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return grade


def submit_data(student_name: str, student_score: float, grade: str):
    """
    The purpose of this function is to open the csv file in write mode and add a header if none exists,
    then writes student info that is inputted from the ui. This is called by the handle_submit in main.py.
    :param student_name: Name of the student represented as a STRING
    :param student_score: Numeric value of student's grade represented as a FLOAT
    :param grade: Letter grade calculated by student score represent with a single character string.
     Appends to CSV file.
    """
    csv_path = 'grades.csv'

    with open(csv_path, mode='a', newline='') as csv_file:
        fieldnames = ['Student Name', 'Student Score', 'Grade']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        if csv_file.tell() == 0:
            writer.writeheader()

        writer.writerow({'Student Name': student_name, 'Student Score': student_score, 'Grade': grade})


def reset_file(csv_file_path: str):
    """
    This functions purpose is to clear a csv file if it exists when it is called on by handle_reset in main.py.
    :param csv_file_path: location of resulting csv file.
    :return:
    """

    try:
        if os.path.exists(csv_file_path):
            os.remove(csv_file_path)
            print("CSV file reset.")
        else:
            print("CSV file does not exist.")
    except Exception as e:
        print(f"Error resetting CSV file: {e}")
