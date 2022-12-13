# course-project-group-88
# CLASSIFY

Group Members: Eli Kujawa (ekujawa2), Pratim Vasireddy (pvv2), Taisia Kalinina (taisiak2)

Classify is a site that allows users to input their schedule and select a subject, and find UIUC courses which fit in their schedules.
Currently, Classify displays classes from the Spring 2023 course catalog.

Classify is a site built using Node.js that is ran on a local server. It utilizes webscraped data on sections of UIUC courses, and a python script which takes a schedule and a subject as an input, and returns the courses and sections which the user could fit into their schedules. 

Our site has 3 main components:

+ The Frontend, primarily made by Taisia Kalinina. The frontend is made up of Javascript, CSS and HTML, using ajax to call the backend. It displays courses that fits within the restrictions inputted by the user. 
+ The Backend, primarily made by Eli Kujawa. The backend is written using python and searches for avaialable courses given the restrictions the user inputs. 
+ The Webscraper, primarily made by Pratim Vasireddy. The webscraper is written in python on uses BeautifulSoup, Selenium, PyPDF, and the Pandas library in order to scrape [course explorer](https://courses.illinois.edu/) for all courses and their meeting times for the given semester.

All of us (Taisia, Pratim, and Eli) were involved in connecting these 3 components.

## Installation

Download the repository into a directory of your choosing by running
```bash
git clone https://github.com/CS222-UIUC/course-project-group-88.git
```
Make sure you have Node.js installed. To check if Node.js is already installed on your device, run
```bash
node -v
```
in your terminal. For installation help, [click here](https://nodejs.org/en/download/).

In your project directory, run
```bash
npx serve
```
and use the first link to travel to the local server.

## Usage

Travel to the local server. As specified on the site, insert times of unavailability into respective table slots. Search the department abbreviations for which courses you would like to see fit into your schedule. Hit the "Show Class Options" button to receive courses that fit within your schedule. To stop running the website, shutdown the terminal.

