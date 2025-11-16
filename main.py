# main.py 

from modules.file_handler import read_data
from modules.grader import process_students
from modules.report_writer import write_report

def main() : 

    print("======== Student Perfomance Tracker ========")
    print("Processing ... Please wait ")

    input_file = "/home/zynx/Documents/student-perfomance-tracker/data/raw_scores.csv"
    output_file = "student-perfomance-tracker-results.txt"

    show_data = read_data(input_file)
    analyze_data = process_students(show_data)
    write_report(analyze_data , output_file)



if __name__  ==  "__main__" :
    main()