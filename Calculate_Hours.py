import sys
import time
import datetime

course_1 = sys.argv[2]
course_2 = sys.argv[3]
print("First course: ", course_1)
print("Second course: ", course_2)

timesheet = "" 
with open(sys.argv[1], 'r') as timesheet_file:
    for line in timesheet_file:
        timesheet += line

# print(timesheet) 
something1 = datetime.timedelta(0)
something2 = datetime.timedelta(0)
timesheet= timesheet.split(";")
del timesheet[-1]
for line in timesheet:
    print(line)
    
    line = line.split(":", 1)
    course = line[0]
    start = datetime.datetime.strptime(line[1].split("-")[0].lstrip(),"%H:%M")
    end = datetime.datetime.strptime(line[1].split("-")[1].rstrip(),"%H:%M")
    if end < start:
        end += datetime.timedelta(days=1)
    if course.__contains__(course_1):
       something1 += end - start 
       print(something1)

    elif course.__contains__(course_2):
       something2 += end - start 
       print(something2)
    

print(course_1, ": ",something1)
print(course_2, ": ",something2)
print(course_1, " + ", course_2, ": ", something1 + something2)