import sys
import time
import datetime

'''
course_name:start_time-end_time;
220:10:00-12:30;
220 Grading : 10:00 - 12:30 ;
'''

course_1 = sys.argv[2]
course_2 = sys.argv[3]
print("First course: ", course_1)
print("Second course: ", course_2)

timesheet = "" 
with open(sys.argv[1], 'r') as timesheet_file:
    for line in timesheet_file:
        timesheet += line

# print(timesheet) 
course_1_time = datetime.timedelta(0)
course_2_time = datetime.timedelta(0)
timesheet= timesheet.split(";")
del timesheet[-1]
for line in timesheet:
    #print(line)
    
    line = line.split(":", 1)
    course = line[0]
    start = datetime.datetime.strptime(line[1].split("-")[0].lstrip(),"%H:%M")
    end = datetime.datetime.strptime(line[1].split("-")[1].rstrip(),"%H:%M")
    if end < start: # Prevents timedelta to go negative
        end += datetime.timedelta(days=1)
    if course.__contains__(course_1):
       course_1_time += end - start 

    elif course.__contains__(course_2):
       course_2_time += end - start 
    

print(course_1, ":",course_1_time)
print(course_2, ":",course_2_time)
print(course_1, "+", course_2, ":", course_1_time + course_2_time)