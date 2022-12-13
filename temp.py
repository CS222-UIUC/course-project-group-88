import requests
import tabula
import os
import csv
from typing import List
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from exception import exceptions

def test(department: str, course: str) :
    url = 'https://courses.illinois.edu/pdf/schedule/' + '2023' + '/' + 'spring' + '/' + department + '/' + course
    response = requests.get(url, stream=True)
    pdf = open('oi.pdf', 'wb')
    pdf.write(response.content)
    pdf.close()
    text = tabula.read_pdf("oi.pdf", pages="all")
    print(text[2])
    os.remove("oi.pdf")

def souper(department: str, course: str):
    url = 'https://courses.illinois.edu/schedule/' + '2022' + '/' + 'fall' + '/' + department + '/' + course
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    #body.find(id="wrap").find(class_="container")
    print(soup.text)

def sel(department: str, course: str):
    url = 'https://courses.illinois.edu/schedule/' + '2023' + '/' + 'spring' + '/' + department + '/' + course
    driver = webdriver.Chrome()
    driver.implicitly_wait(400)
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    driver.close()
    app_meetings = soup.find_all(class_="app-meeting")
    return clean(app_meetings)

def clean(data) -> List[str] :
    return_me = []
    for datum in data:
        breakless = str(datum).replace("<br/>", "&")
        cleaned = ""
        split = False
        for character in breakless :
            if character == '>' and split:
                split = False
            elif character == '<' :
                split = True
            elif not split :
                cleaned += character
        if cleaned.endswith("&") :
            cleaned = cleaned[:-1]
        if cleaned.startswith("&") :
            cleaned = cleaned[1:]
        if cleaned.endswith('"') :
            cleaned = cleaned[:-1]
        if cleaned.startswith('"') :
            cleaned = cleaned[1:]
        return_me.append(cleaned.strip())
    return return_me


if __name__ == '__main__':
    courses = pd.read_csv("courses.csv")
    department = courses.loc[(courses['DepartmentAbbreviation'] < 'PATH') & (courses['DepartmentAbbreviation'] >= 'ME')]
    #& (courses['DepartmentAbbreviation'] > 'ASST')
    #for dat in range(len(department)):
        #print(department.iloc[dat, 2])
    with open('current.csv', 'w', encoding='UTF8', newline='') as file:
        writer = csv.writer(file)

        #writer.writerow(['DepartmentAbbreviation', 'CourseNumber', 'CourseName', 'Type', 'Section', 'Time', 'Day', 'Location', 'Instructor'])
        for course_idx in range(len(department)):
            base = [str(department.iloc[course_idx, 0]), int(department.iloc[course_idx, 1])]
            if base[0] == 'MUSC' or base in exceptions:
                continue
            information = sel(base[0], str(base[1]))
            base.append(str(department.iloc[course_idx, 2]))
            for i in range(len(information) // 6):
                idx = i * 6
                info = base.copy()
                if information[idx+2] == information[idx+3] :
                    print(base)
                    break
                else :
                    info.append(information[idx])
                    info.append(information[idx+1])
                    info.append(information[idx+2])
                    info.append(information[idx+3])
                    info.append(information[idx+4])
                    info.append(information[idx+5])
                    print(info)
                    writer.writerow(info)
    print("done")