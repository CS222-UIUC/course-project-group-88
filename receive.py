import sys

def test(check) :
    return check[0:2] + " test"

input = sys.argv[1] #receives js string
print(input.split('m')) #whatever you want to export back to the js file
sys.stdout.flush()
