from PyQt5 import QtWidgets
from grade_calculator_gui import Ui_MainWindow
from logic import *
import sys


class GradeCalculatorApp(QtWidgets.QMainWindow, Ui_MainWindow):



    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button_submit.clicked.connect(self.handle_submit)
        self.button_reset.clicked.connect(self.handle_reset)

    def handle_submit(self):

        """ This function's purpose is to grab the student name and score from gui. It also ensure the correct
        data types are entered. Then calls submit_data function in logic.py.

        :return:
        """
        student_name = self.input_line_student_name.text()
        student_score_text = self.input_line_student_grade.text()

        try:
            if any(char.isdigit() for char in student_name):
                raise ValueError("Invalid student name. \nPlease enter a string")

            student_score = float(student_score_text)
            grade = grade_scale(student_score)

            submit_data(student_name, student_score, grade)
            self.label_output.setText(f"Data submitted: {student_name}, {student_score}, {grade}")
        except ValueError as e:
            self.label_output.setText(str(e))
        except Exception as e:
            self.label_output.setText('An error occurred: {e}')



    def handle_reset(self):
        """
        The purpose of this function is to clear the gui's input boxes and call on reset_file in logic.py
        to reset the csv when the reset button in the UI is pressed.
        :return:
        """

        csv_file_path = 'grades.csv'

        self.input_line_student_name.clear()
        self.input_line_student_grade.clear()
        self.label_output.clear()

        try:
            reset_file(csv_file_path)
            self.label_output.setText("File reset.")
        except FileNotFoundError:
            self.label_output.setText(f"File not found: {csv_file_path}")
        except Exception as e:
            self.label_output.setText(f"An error has occurred. {e}")


def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = GradeCalculatorApp()
    main_window.show()

    try:
        sys.exit(app.exec_())
    except Exception as e:
        print(f"An error has occurred: {e}")


if __name__ == "__main__":
    main()
