import requests
from bs4 import BeautifulSoup
#print(bs4)

URL = "https://courses.illinois.edu/schedule/DEFAULT/DEFAULT"
page = requests.get(URL)

#print(page.text)

soup = BeautifulSoup(page.content, "html.parser")

courses = soup.find(class_="table-responsive")
#print(courses.prettify())

#courses2 = courses.find_all("a")
#for x in courses2:
#    print(x.text.strip())

coursecodes = courses.find_all("td")
for y in coursecodes:
    print(y.text.strip())


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

"""class Course:
    def """


