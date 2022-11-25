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
print(urmom)

urmom.setUnavailable("MWF", 8.0)
print(urmom)

print(str(urmom.checkAvailable((7.0, 9.0), "TR")))
print(str(urmom.checkAvailable((7.0, 9.0), "MWF")))