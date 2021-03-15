'''
This code takes the sata from a text document and creates an excel sheet
'''
import numpy as np
import pandas as pd
myfile = open("C:\\Users\\skoli\\Documents\\bits_projects_list\\courseslist.txt","r",encoding='utf-8')
myfile.seek(0)
mylist = myfile.readlines()
myfile.close()
newlist = []
course_no = []
course_title = []    
L =[]
P = []
U = []
for i in range(1,len(mylist)):
    string = mylist[i].split()
    string = [' '.join(string[:2]),' '.join(string[2:-3]), string[-3:]]
    course_no.append(string[0])
    course_title.append(string[1])
    L.append(string[2][0])
    P.append(string[2][1])
    U.append(string[2][2])
d = {'Course Number': course_no , 'Course Title': course_title, 'L':L, 'P':P,'U':U}
df = pd.DataFrame(data=d)
df = df.drop_duplicates(subset = 'Course Number', keep = 'first')
df = df.sort_values(by = 'Course Number')
df.reset_index(drop=True, inplace=True)
df.to_excel("C:\\Users\\skoli\\Documents\\bits_projects_list\\bitscourses_excel.xlsx",engine='xlsxwriter')   
df.to_csv("C:\\Users\\skoli\\Documents\\bits_projects_list\\bitscourses_csv.csv")   