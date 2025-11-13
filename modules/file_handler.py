# Reads data , handle missing files and invalid data 

def read_data ( file_path ) : 
    #  an empty list to store the cleaned data after reading
    cleaned_data = []

    try : 
        with open ( file_path , "r") as file : 
            """
            The CSV file has an header/fieldname along with the names and  score so we have to split those first
             The first is to get the headers , then get the names and scores( then split)
            """
            content = [ file.readline().strip() ]

            if content : 
                for line in file : 
                    parts =  line.strip().split(',') 

                    if len( parts ) > 1 : 
                        name = [ parts[0].strip() ]

                    scores = []
                    for x in parts[1:] :
                        try : 
                            score = float(x)
                        except ValueError: 
                            print(f"⚠️ Invalid score: '{x}' found — replaced with 0.")
                            score = 0
                        scores.append(score)


                    cleaned_data.append(( name , scores ))
                

            if not cleaned_data : 
                raise ValueError("File is empty")        
            return cleaned_data
            
            
    except FileNotFoundError : 
        print("File not found")      

input_file = "/home/zynx/Documents/student-perfomance-tracker/data/raw_scores.csv"

show_file = read_data(input_file)

print(show_file)

