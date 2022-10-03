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

class Section(Course):
    def __init__(self, section_code, time, linked, location, professor, course_name, number, subject, subject_code):
        super().__init__(course_name, number, subject, subject_code)
        self.section_code = section_code
        self.time = time
        self.linked = linked
        self.location = location
        self.professor = professor

    def RateMyProfessorRating(URL):
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        y = soup.find(class_="RatingValue__Numerator-qw8sqy-2 liyUjw")
        return y.text.strip()
        


