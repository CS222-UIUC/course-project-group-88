import csv

val = input("Class concise schedule copy & paste: ")
header = ['num', 'full_title', 'time', ]
with open('my_sched.csv', 'w', encoding='UTF8', newline = ' ') as f:
   writer = csv.writer(f)
   
