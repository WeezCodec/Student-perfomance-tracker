# modules /graders.py

def calc_average (scores) : 
    # return average of a list of scores.
    return sum ( scores) / len ( scores)


def assign_grade( average ) : 
    # assigns grade to the average scores collected from the list.
    if average >= 75 :
        return "A"
    elif average >= 65 : 
        return "B"
    elif average >= 55 : 
        return "C"
    elif average >= 45 : 
        return "D"
    else : 
        return "F"
    

# return cleaned up result 

def process_students( student) : 
    """
    Takes in [name , [scores. ....]] and returns [(name) , (average)  (grade)]
    """
    result = []

    for name , scores in student : 
        avg = calc_average ( scores)
        grade = assign_grade(avg)
        result.append ((name , round(avg , 2)  , grade))

    return result    
    

