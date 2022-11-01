import requests
import tabula
import os
from typing import List

def split_at_num(phrase: str) -> List[str] :
    return_me = [""]
    rec_num = True
    idx = 0
    for cha in phrase:
        if cha.isnumeric() and rec_num:
            return_me[idx] = return_me[idx] + cha
        else:
            if cha.isnumeric():
                idx += 1
                return_me.insert(idx, cha)
            else : 
                return_me[idx] = return_me[idx] + cha    
        rec_num = cha.isnumeric()       
    return return_me


def course_info(department: str, course_num: str, year='2022', sem="fall"):
    url = 'https://courses.illinois.edu/pdf/schedule/' + year + '/' + sem + '/' + department + '/' + course_num
    response = requests.get('https://courses.illinois.edu/pdf/schedule/2022/fall/ARTS/243', stream=True)
    pdf = open('oi.pdf', 'wb')
    pdf.write(response.content)
    pdf.close()
    sections = []
    text = tabula.read_pdf("oi.pdf", pages="all")
    for frame in text:
        for sec in frame['Section'].dropna() :
            sections.insert(int(sec), [int(sec), 0, "", 0, ""])
        for i, days in enumerate(frame['Days'].dropna()) :
            sections[i][1] = days
        for i, time in enumerate(frame["Time"].dropna()):
            if i % 2 == 0:
                sections[i//2][2] = time
            else :
                sections[i//2][2] = sections[i//2][2] + time
        locations = ""
        for location in frame["Location"].dropna():
            locations += location + " "
        for i, loc in enumerate(split_at_num(locations)):
            sections[i][3] = loc
        idx = 0
        for people in frame["Instructor"].dropna():
            sections[idx][4] = sections[idx][4] + (" " if "," in people and sections[idx][4] != "" else "") + people
            if ',' in people:
                idx += 1
        print(sections)
    os.remove("oi.pdf")
    

if __name__ == '__main__':
    course_info('ARTS', '243')
    