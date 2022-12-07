# SIMPLE FUNCTION TESTS
# testing daysToIdx
print("dayToIdx test\n")
print(f"{dayToIdx('M')} \n")
print(f"{dayToIdx('T')} \n")
print(f"{dayToIdx('W')} \n")
print(f"{dayToIdx('R')} \n")
print(f"{dayToIdx('F')} \n")

for i in days_arr:
    print(f"{i} is at index {dayToIdx(i)}")

# testing idxToDay
print("\nidxToDay test\n")
for j in range(0, 5):
    print(f"The {j}-th day is " + days_arr[j])

# testing timeToIdx:
print("\ntimeToIdx test\n")
for i in range(14, 44):
    i = i/2.0
    print(f"time {i} is at index {timeToIdx(i)}")

# testing idxToTime:
print("\nidxToTime test\n")
for i in range(0, 30):
    print(f"idx {i} stores time {idxToTime(i)}")


# SCHEDULE TEST

urmom = Schedule()

for i in range(14, 18):
    i = i/2.0
    urmom.setUnavailable("MTWRF", i)

urmom.setUnavailable("MWF", 11)
urmom.setUnavailable("MWF", 11.5)
for i in range(24, 30):
    i = i/2.0
    urmom.setUnavailable("W", i)

for i in range(18, 24):
    i = i/2.0
    urmom.setUnavailable("TR", i)

urmom.setUnavailable("TR", 7.5)
urmom.setUnavailable("M", 10)


print(urmom)

print(str(urmom.checkAvailable((7.0, 9.0), "TR")))
print(str(urmom.checkAvailable((7.0, 9.0), "MWF")))

aas = readFile('.github/bigboi.csv', "CS")

print(aas)

print(nearestTimes([3.50, 5.5]))

for i in aas.courses[0].sections:
    for j in i:
        print(urmom.checkAvailable(nearestTimes(j.time), j.days))

x = classWorks(aas.courses[0], urmom)

'''for a in x:
    for b in a:
        print(str(b))'''

y = subjectOptions(aas, urmom)

for a in y:
    #print(key)
    for b in a:
        for c in b:
            print(str(c))
            
print(y)

print(makeDictForJSON(y))

#with open("sample.json", "w") as outfile:
urmom2 = json.dumps(makeDictForJSON(y), indent = 4)
print(urmom2)

with open("sample.json", "w") as outfile:
    json.dump(makeDictForJSON(y), outfile)
    
atlasSched = Schedule()

for i in range(22, 26):
    i = i/2
    atlasSched.setUnavailable("MWF", i)
    
for i in range(28, 32):
    i = i/2
    atlasSched.setUnavailable("MWF", i)
    
for i in range(22, 24):
    i = i/2
    atlasSched.setUnavailable("TR", i)
    
print(json.dumps(makeDictForJSON(subjectOptions(readFile(".github/bigboi.csv", "CS"), atlasSched)), indent = 4))