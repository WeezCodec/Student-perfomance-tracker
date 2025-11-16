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
        s.append(s)


# def write_report (result , output_file) : 
#     try : 

    #     with open ( output_file , "w") as file : 

    #         file.write("Name\tAverage\tGrade\n")
    #         file.write("="*30 + "\n")

    #         for name , avg , grade in result : 
    #             file.write ( f"{name}\t{avg}\t{grade}\n" )

    #     print(f"Report successfully written to {output_file}")        

    # except Exception as e : 
    #     print(f"Error writing report {e}")   
        