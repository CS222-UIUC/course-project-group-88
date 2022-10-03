from optparse import IndentedHelpFormatter
import os
import requests

import PDfplumber
from bs4 import BeautifulSoup
from typing import List, Tuple

def get_departments(url: str) -> List[Tuple[str, str]]:
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    departmentTable = soup.find(class_="table-responsive")
    departments = departmentTable.findAll("td")
    long_string = ""
    for i, department in enumerate(departments):
        long_string += department.text.strip()
        if i % 2 == 1:
            long_string += "\n"
        else: 
            long_string += "\t"
    together = [tuple(labels.split("\t")) for labels in long_string.split("\n")[:-1]]
    return together

def get_courses(departmentURL : str) ->List[Tuple[str, str]] :
    page = requests.get(departmentURL)
    soup = BeautifulSoup(page.content, "html.parser")
    courseTable = soup.find(class_="table-condensed")
    courses = courseTable.findAll("td")
    long_string = ""
    for i, course in enumerate(courses):
        long_string += course.text.strip()
        if i % 2 == 1:
            long_string += "\n"
        else: 
            long_string += "\t"
    together = [tuple(labels.split("\t")) for labels in long_string.split("\n")[:-1]]
    return together

def get_course_info(courseURL : str) :
    page = requests.get(courseURL)
    soup = BeautifulSoup(page.content, "html.parser")
    #print(soup.p)
    infoTable = soup.findAll("tr")
    courseInfo = infoTable #.findAll("td")
    return courseInfo


if __name__ == '__main__' :
    response = requests.get('https://courses.illinois.edu/pdf/schedule/2022/fall/ARTS/243', stream=True)
    pdf = open('oi.pdf', 'wb')
    pdf.write(response.content)

   # pdfReader = PyPDF2.PdfFileReader(pdf)
    with PDfplumber.open('oi.pdf') as info:
        firstPage = info.pages[0]
        print(firstPage.extract_text())
    pdf.close()
    os.remove('oi.pdf')

    #print(get_course_info('https://courses.illinois.edu/schedule/2022/fall/ARTS/243'))