# testing

# subject class test -- passes!
math = Subject("Math", "MATH")
print(math.__str__())
math.getCourses()

# course class test
abs_alg = Course("Intro to Abstract Algebra", "417", "Math", "MATH")
print(abs_alg.__str__())

# section class test
# [using fake data]
abs_alg_B13 = Section("B13", ["M", "W", "F"], (9.00, 9.83), False, "HAB", "Matthew Russell", "Intro to Abstract Algebra", "417", "Math", "MATH")
print(abs_alg_B13.__str__())

