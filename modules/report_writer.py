# modules / report_writer.py

def write_report (result , output_file) : 
    try : 

        with open ( output_file , "w") as file : 

            file.write("Name\tAverage\tGrade\n")
            file.write("="*30 + "\n")

            for name , avg , grade in result : 
                file.write ( f"{name}\t{avg}\t{grade}\n" )

        print(f"Report successfully written to {output_file}")        

    except Exception as e : 
        print(f"Error writing report {e}")   
        