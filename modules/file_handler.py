import csv


def read_data( file_name) :

    cleaned_data = []      # this is where we store the cleaned data in

    try : 
        with open ( file_name , "r"  ) as file : 
            content = csv.DictReader( file )
            content.fieldnames = [ name.lower().strip() for name in content.fieldnames ] 

            for row in content : 
                cleaned_data.append ({
                    "name" : row["name"] , 
                    "math" : float(row["math"]) , 
                    "english" : float(row["english"]) ,
                    "science" : float(row["science"]) , 
                    "history" : float(row["history"])
                })

            if not cleaned_data :
                raise ValueError(" File is empty ")
            
            return cleaned_data



    except FileNotFoundError :
        print("File not Found")

input_file = "raw_scores.csv"
read_data(input_file)

