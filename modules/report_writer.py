# modules / report_writer.py

from grader import Student
from file_handler import read_data
import os
import csv


def process_scores(input_file) : 
    show_data = read_data(input_file)

    result = []

    for name , scores in show_data : 
        s = Student(name , scores)
        s.calc_average()
        s.assign_grade()
        result.append(s)


  # Ensures report folder exists
    try : 
        os.mkdir("reports" , exist_ok = True)
        output_file = "reports/student-perfomance-tracker-results.csv"

        with open(output_file , "w" , newline= "") as file : 
            content = csv.writer ( file )
            content.writerow(["Name" , "Average" , "Grade"])
            
            for s in Student : 
                content.writerow([s.name , f"{s.average:.2f}", s.grade])

        print(f"Report generated : {output_file}")         

    except Exception as e : 
        print("Error while writing to file {e}")

        

