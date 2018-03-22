import json
import sys

with open(sys.argv[1]) as jsonData:
    dzialanie = json.load(jsonData)

numbers = dzialanie['numbers']
operation = str(dzialanie['operation'])

print str(numbers[0])+operation+str(numbers[1])
print '='
print eval(str(numbers[0])+operation+str(numbers[1]))




