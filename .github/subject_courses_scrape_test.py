import requests
from bs4 import BeautifulSoup

URL = "https://courses.illinois.edu/schedule/2022/fall/AAS"
page = requests.get(URL)

print(page.text)

soup = BeautifulSoup(page.content, "html.parser")

courses = soup.find(class_="table table-striped table-bordered table-condensed")

coursecodes = courses.find_all("td")
for y in coursecodes:
    print(y.text.strip())