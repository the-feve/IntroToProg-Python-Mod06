# --------------------------------------------------------------------------- #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   MFevergeon,8/17/2025,Created Script
#   <Your Name Here>,<Date>,<Activity>
# --------------------------------------------------------------------------- #
import json
import io

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# FILE_NAME: str = "Enrollments.csv"
FILE_NAME: str = "Enrollments.json"


# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str = ''  # Hold the choice made by the user.

# Define the Data Variables and constants
# Removed all of these and used them locally instead
    # student_first_name: str = ''  
    # student_last_name: str = '' 
    # course_name: str = ''  # Holds the name of a course entered by the user.
    # student_data: dict = {}  # one row of student data

    # file = None  # Holds a reference to an opened file.


# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    MFevergeon,8.17.2025,Created Class
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        This function reads student data from a JSON file.
        
        ChangeLog: (Who, When, What)
        MFevergeon,8.17.2025,Created Class
        """
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages(
                "Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        This function writes student data to a JSON file.

        ChangeLog: (Who, When, What)
        MFevergeon,8.17.2025,Created Class
        """

        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            print() #space added for clarity
            print(f"The following data was written to file:")
            print() #space added for clarity
            for student in student_data:
                print(f"{student['FirstName']}, {student['LastName']},"
                    f" {student['CourseName']}"
                    )
            file.close()
        except TypeError as e:
            IO.output_error_messages(
                "Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()

# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and 
    output

    ChangeLog: (Who, When, What)
    MFevergeon,8.17.2025,Created Class and contained methods
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays a custom error messages to the user

        ChangeLog: (Who, When, What)
        MFevergeon,8.17.2025,Created function

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the a menu of choices to the user

        :return: None

        ChangeLog: (Who, When, What)
        MFevergeon,8.17.2025,Created function
        """
        print()
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        :return: string with the users choice
        
        ChangeLog: (Who, When, What)
        MFevergeon,8.17.2025,Created function
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing the exception 
                                       # object to avoid the technical message

        return choice

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets student data from the user

        :return: dictionary with the student's data
        
        ChangeLog: (Who, When, What)
        MFevergeon,8.17.2025,Created function
        """
        student_data = {}
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("First name must contain only letters.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("Last name must contain only letters.")
            course_name = input("Please enter the name of the course: ")
            if not course_name:
                raise ValueError("Course name cannot be empty.")

            student_data = {
                "FirstName": student_first_name,
                "LastName": student_last_name,
                "CourseName": course_name}
        except ValueError as e:
            IO.output_error_messages(e.__str__())
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)

        return student_data

    @staticmethod
    def output_student_courses(student_data: list):
        """ This function displays the courses for each student

        :return: None
        """
        for student in student_data:
            print(
                f'{student["FirstName"]},'
                f'{student["LastName"]}, '
                f'{student["CourseName"]}'
            )


# When the program starts, read the file data into a list of lists (table)

try: 
    students = FileProcessor.read_data_from_file(
        file_name=FILE_NAME, student_data=students)
except Exception as e:
    IO.output_error_messages("There was a problem with reading the file.", e)

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        student_data = IO.input_student_data(students)
        students.append(student_data)

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(FILE_NAME, students)

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
