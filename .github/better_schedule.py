from typing import List, Tuple

days_arr = ['M', 'T', 'W', 'R', 'F']

def dayToIdx(day: chr) -> int:
    for i in range(0, 5):
        if days_arr[i] == day:
            return i
    return -1

def idxToDay(idx: int) -> chr:
    return days_arr[i]

# Class storing the user's schedule
# Member variables:
# 2D 5x30 array of bools, representing availability of half-hour timeslots from 7am to 10pm
# array of Course objects of the courses the user is already in
class Schedule:
    # reads a schedule from a CSV file and converts it to schedule object
    def __init__(self):
        # TO DO ONCE I HAVE THE CSV
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
    
    def checkAvailable(self, time: Tuple[float, float], days: str) -> bool:
        for i in range(timeToIdx(time[0]), timeToIdx(time[1])):
            for j in days:
                if not self.sched[dayToIdx(j)][i]:
                    return False
        return True
    
"""
Functions for converting from time to idx in schedule array and vice versa
"""
def timeToIdx(time: float) -> int:
    return (int)(time - 7)*2

def idxToTime(idx: int) -> float:
    return (idx * 1.0)/2 + 7


"""
checks if a class at class_time on days works in a schedule
"""
def classWorks(class_time: Tuple[float, float], days: str, schedule: Schedule):
    for i in range(timeToIdx(class_time[0]), timeToIdx(class_time[1])):
        for j in days:
            if not schedule.sched[j][i]:
                return false
    return true
        

# run test file
exec(open(".github/better_schedule_TESTS.py").read())