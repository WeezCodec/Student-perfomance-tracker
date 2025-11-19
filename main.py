# main.py 

from modules.report_writer import process_scores

def main() : 

    print("======== Student Perfomance Tracker ========")
    print("Processing ... Please wait ")

process_scores("/home/zynx/Documents/student-perfomance-tracker/data/raw_scores.csv")


if __name__  ==  "__main__" :
    main()