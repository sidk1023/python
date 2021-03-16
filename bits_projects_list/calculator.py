import pandas as pd
import numpy as np
evs = False
df = pd.read_csv("bitscourses_csv.csv")
grades = {'E':2, 'D':4, 'C-':5, 'C':6, 'B-':7, 'B':8, 'A-':9, 'A':10, 'NC':0, 'P/F':0} 
class Course_Calculator:
    def __init__(self, cgpa=0,total_creds=0,courses = [],prev_creds=0,prev_cgpa=0):
        self.cgpa = cgpa
        self.total_creds = total_creds+prev_creds
        self.courses = courses
        self.prev_creds = prev_creds
        self.prev_cgpa = prev_cgpa
   
        
    def find_course(self):
        while True:
            flag = True
            course = input("Enter the course code or Title: ")
            for i in range(len(df)):
                if (course.lower() == df.iloc[i,1].lower()) or (course.lower() == df.iloc[i,2].lower()):
                    while True:
                        grade = input("enter the grade: (enter 0 for P/F) ")
                        if grade in grades.keys():
                            mygrade = grades[grade]
                            break
                        elif int(grade) in grades.values():
                            mygrade = int(grade)
                            break
                        else:
                            print("enter a valid grade among the following; 'E':2, 'D':4, 'C-':5, 'C':6, 'B-':7, 'B':8, 'A-':9, 'A':10, 'NC':0, P/F:0")
                            continue
                    newlist = [df.iloc[i,1],df.iloc[i,2],int(df.iloc[i,5]),mygrade] 
                    if newlist in self.courses:
                        flag = False
                        print("Course is already entered")
                        break
                        
                    else:
                        self.courses.append(newlist)
                        
                        self.total_creds=self.total_creds+int(df.iloc[i,5])  #adjust for evs later
                        flag = False
                        break
                        
            if flag:
                print("Enter a valid course")
                continue
            else:
                break
    def display(self):
        print("Total credits = " + str(self.total_creds))
        self.calculate_cgpa()
        print("CGPA = "+ str(self.cgpa))
        
    def find_all_courses(self):
        while True:
            self.display()
            self.find_course()
            Flag = True
            while Flag:
                cont = input("Enter a course/ print?: [y/n/p]").lower()
                if cont == 'y':
                    Flag = True
                    break
                elif cont == 'n':
                    Flag = False
                    break
                elif cont == 'p':
                    print(self)
                    continue
                else:
                    print("please enter y, n or p")
                    continue
            if Flag:
                continue
            else:
                break
    def adjust_evs(self):
        global evs
        for mylist in self.courses:
            if ("BITS F225" in mylist) :
                evs = 3
                break
            else:
                evs = 0               
    def calculate_cgpa(self):
        total = (self.prev_creds-evs1)*self.prev_cgpa
        for mylist in self.courses:
            total = total + mylist[2]*mylist[3] 
        
        self.adjust_evs()   
        try:
            self.cgpa = float(total/(self.total_creds-evs-evs1))
        except ZeroDivisionError  :  
            self.cgpa = 0
    def __str__(self):
        return "CGPA: %s, Total Credits: %s,\nCourses: \n%s" %(self.cgpa, self.total_creds, self.courses)
   
    def delete_course(self, course):
        for i in range(len(self.courses)):
            if course in self.courses[i]:
                self.courses.pop(i)
print("Welcome to BITS CGPA Calculator\n")
while True:
    try:
        prev_cg = float(input("please enter your CGPA till the previous Semester correct to two decimal places: \n"))
        prev_credits = int(input("please enter your total completed credits: \n"))
        while True:
                cont= input("Have you completed evs?: [y/n]").lower()
                if cont == 'y':
                    evs1 = 3
                    break
                elif cont == 'n':
                    evs1=0
                    break
                else:
                    print("please enter y or n")
                    continue
        
    except ValueError:
        print("Please enter a float for CGPA and an int for completed credits")
    else:
        break
calc = Course_Calculator(prev_creds= prev_credits,prev_cgpa=prev_cg)
calc.find_all_courses()                