from typing import List, Tuple
import csv

days_arr = ['M', 'T', 'W', 'R', 'F']

"""
Functions for converting from day (of week) to idx in days_arr and vice versa
"""
def dayToIdx(day: chr) -> int:
    for i in range(0, 5):
        if days_arr[i] == day:
            return i
    return -1

def idxToDay(idx: int) -> chr:
    return days_arr[i]  

"""
Functions for converting from time to idx in schedule array and vice versa
"""
def timeToIdx(time: float) -> int:
    if(time - int(time) == 0):
        return (int)(time - 7)*2
    else:
        return (int)(time-7)*2 + 1

def idxToTime(idx: int) -> float:
    return (idx * 1.0)/2 + 7

"""
Function to convert from string in format "XX:XX{AM/PM} - XX:XX{AM/PM}" to time double tuple
"""
def strToTime(timestring: str) -> tuple:
    parts = timestring.split(' ')
    t1str = parts[0]
    t1 = int(t1str[0:2]) + (int(t1str[3:5])/60.0)
    if(t1str[5:7] == "PM" and t1str[0:2] != "12"):
        t1 += 12
    t2str = parts[2]
    t2 = int(t2str[0:2]) + (int(t2str[3:5])/60.0)
    if(t2str[5:7] == "PM" and t2str[0:2] != "12"):
        t2 += 12
    return [t1, t2]

"""
Returns the nearest possible times
"""
def nearestTimes(times: tuple) -> tuple:
    first = ((int)(times[0]*2))/2.0
    if ((int)(times[1]*2))*1.0 - (times[1]*2.0) != 0:
        second = ((int)(times[1]*2)+1)/2.0
        return [first, second]
    else:
        second = ((int)(times[1]*2))/2.0
        return [first, second]

# Class storing the user's schedule
# Member variables:
# 2D 5x30 array of bools, representing availability of half-hour timeslots from 7am to 10pm
# array of Course objects of the courses the user is already in
class Schedule:
    # reads a schedule from a CSV file and converts it to schedule object
    def __init__(self):
        # WILL BE UPDATED ONCE I HAVE A SAMPLE SCHEDULE CSV
        self.sched = []
        base = [True] * 30
        for i in range(0, 5):
            self.sched.append(base.copy())

    def __str__(self):
        sched_str = "\t"
        for i in range(0, 30):
            sched_str += f"{idxToTime(i)}\t"
        for i in range(0, 5):
            sched_str+="\n"
            sched_str += f"{days_arr[i]}:\t"
            for j in range(0, 30):
                sched_str += str(self.sched[i][j]) + "\t"
        return sched_str

    
    # sets a time as "unavailable" if a user has an obligation during that time
    def setUnavailable(self, dayss: str, time: float):
        for i in range(0, len(dayss)):
            self.sched[dayToIdx(dayss[i])][timeToIdx(time)] = False
    
    # checks if a user is available in a given time slot on a given set of days
    def checkAvailable(self, time: Tuple[float, float], days: str) -> bool:
        for i in range(timeToIdx(nearestTimes(time)[0]), timeToIdx(nearestTimes(time)[1])):
            for j in days:
                if not self.sched[dayToIdx(j)][i]:
                    return False
        return True




class Section:
    def __init__(self, time: str, days: str, thetype: str):
        self.timestr = time
        self.time = strToTime(self.timestr)
        self.days = days
        self.type = thetype
    
    def __str__(self):
        return self.timestr + " ; " + self.days

     
'''class Subject:
    def __init__(self, filename):
        # reads file and makes a bunch of stuff'''
    
class Course:
    def __init__(self, number: int, name: str):
        self.number = number
        self.name = name
        self.numtypes = 0
        self.sections = []

    def __str__(self):
        to_return = f"{self.number}: {self.name}\n{self.numtypes} types\n"
        for classtype in self.sections:
            if(classtype):
                to_return += classtype[0].type + ":\n"
                for sec in classtype:
                    to_return += str(sec) + "\n"
        return to_return

    def nameString(self) -> str:
        return f"{self.name} {self.number}"
        

    def addSection(self, sec: Section):
        found = False
        for classtype in self.sections:
            if(classtype) and classtype[0].type == sec.type:
                classtype.append(sec)
                found = True
        if not found:
            newarr = [sec]
            self.sections.append(newarr)
            self.numtypes += 1

class Subject:
    def __init__(self, name: str, code: str):
        self.name = name
        self.code = code
        self.courses = []
    
    def __str__(self):
        to_return = f"{self.code} : {self.name}\n"
        for course in self.courses:
            to_return += str(course) + "\n"
        return to_return

    def addClass(self, course: Course):
        self.courses.append(course)

#def strToTime(time: str) -> Tuple[float, float]:
    # takes time str and returns time represented as a tuple of floats

def readFile(filename) -> Subject:
    with open(filename, mode = 'r') as file:
        urmom = csv.reader(file)
        curnum = -1
        curclass = Course(69, "urmomology")
        subj = Subject("Asian American Studies", "AAS")
        for lines in urmom:
            if len(lines[5]) > 8 and lines[5][8] == '-':
                if curnum != lines[1]:
                    curnum = lines[1]
                    curclass = Course(lines[1], lines[2])
                    subj.addClass(curclass)
                to_add = Section(lines[5], lines[6], lines[3])
                curclass.addSection(to_add)
            #print(to_add)
    return subj

"""
checks if a class at class_time on days works in a schedule

def classWorks(class_time: Tuple[float, float], days: str, schedule: Schedule):
    for i in range(timeToIdx(class_time[0]), timeToIdx(class_time[1])):
        for j in days:
            if not schedule.sched[j][i]:
                return false
    return true
"""
def classWorks(course: Course, sched: Schedule) -> [[]]:
    options = []
    options.append([course.nameString()])
    for class_type in course.sections:
        cando = []
        if len(class_type) != 0:
            cando.append(class_type[0].type)
        for sec in class_type:
            if(sched.checkAvailable(sec.time, sec.days)):
                cando.append(sec)
        if(len(cando) == 0):
            return [["NO VIABLE SECTIONS"]]
        options.append(cando)
        
    #print(options)
    return options

'''def subjectOptions(subject: Subject, sched: Schedule):
    output = []
    for course in subject.courses:
        output.append(courseWorks(course, sched))
    return output'''
    




# run test file
exec(open(".github/better_schedule_TESTS.py").read())