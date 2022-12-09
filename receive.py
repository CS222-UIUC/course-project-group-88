import sys

def test(check) :
    return check[0:2] + " test"

input = sys.argv[1]
print(test(input))
sys.stdout.flush()
