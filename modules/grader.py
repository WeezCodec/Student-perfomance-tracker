# modules / grader.py

class Student : 
    def __init__ (self , name , scores ) : 
        self.name = name 
        self.scores = scores 
        self.average = 0
        self.grade = ""

    def calc_average( self )  : 
        self.average = sum(self.scores) / len(self.scores)

    def assign_grade(self) : 
        avg = self.average

        if avg >= 75 : 
            self.grade = "A"
        elif avg >= 65 : 
            self.grade = "B"
        elif avg >= 55 : 
            self.grade ="C"
        elif avg >= 45 :
            self.grade = "D"
        elif avg >= 40 : 
            self.grade = "E"
        else : 
            self.grade = "F"
