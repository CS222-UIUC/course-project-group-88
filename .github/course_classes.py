from operator import truediv
import requests
from bs4 import BeautifulSoup

class Subject:
    def __init__(self, subject, subject_code, semester="fall", year="2022"):
        self.subject = subject
        self.subject_code = subject_code
        self.URL = "https://courses.illinois.edu/schedule/" + year  + "/" + semester +"/" + subject_code

    def __str__(self):
        return self.subject + ": " + self.URL

    def getCourses(self):
        page = requests.get(self.URL)
        soup = BeautifulSoup(page.content, "html.parser")
        courses = soup.find(class_="table table-striped table-bordered table-condensed")
        coursecodes = courses.find_all("td")
        for y in coursecodes:
            print(y.text.strip())

class Course(Subject):
    def __init__(self, name, number, subject, subject_code):
        super().__init__(subject, subject_code)
        self.name = name
        self.number = number


    def __str__(self):
        return self.subject_code + self.number + ": " + self.name

# time = touple of doubles
class Section(Course):
    def __init__(self, section_code, days, time, linked, location, professor, course_name, number, subject, subject_code):
        super().__init__(course_name, number, subject, subject_code)
        self.section_code = section_code
        self.time = time
        self.days = days
        self.linked = linked
        self.location = location
        self.professor = professor

    def RateMyProfessorRating(URL):
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        y = soup.find(class_="RatingValue__Numerator-qw8sqy-2 liyUjw")
        return y.text.strip()
        
# classes: array of sections
# unavailable_times: array of tuples of doubles representing times
class Schedule:
    def __init__(self, classes, unavailable_times):
        self.classes = classes
        self.unavailable_times = unavailable_times

    """def MakeDayArray():
        day = []
        for i in range(7, 10.25, 0.25):
            day.append(i)
        return day
    
    def FindAvailableTimes():
        available_times = []
        for i in range(0, 5):
            day = Schedule.MakeDayArray()
            for class in classes:
                start = (float)((int)(4 * class.time[0])) / 4"""
    def IsOnDay(self, class, day):
        for i in class.days:
            if day == i:
                return True
        return False

    def FindAvailableTimes(self, day):
        available_times = [(7.0, 10.0)]
        for class in self.classes:
            if self.IsOnDay(class, day):
                for time in available_times:
                    if class.time[0] > time[0]:
                        available_times.remove(class)
                        available_times.append((time[0], class.time[0]))
                    if class[1] > time[1]:
                        available_times.remove(class)
                        available_times.append((class.time(1), time(1)))
        return available_times

    
    def SectionWorks(self, section):
        #weekdays = ["mon", "tues", "wed", "thurs", "fri"]
        for day in section.days:
            times = FindAvailableTimes(self, day)
            for time in FindAvailableTimes:
                if time[0] < section.time[0]:
                    if time[1] > section.time[1]:
                        return True
        return False

    

