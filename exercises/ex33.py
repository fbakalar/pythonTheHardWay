#---------------------------------------------------------|
#
#  Exercise 33  While Loops
#   
#  While loops run until a defined condition is met
#
#  is rarely used in python because 'for' loop is 
#  so powerful
#
#---------------------------------------------------------|

i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i+1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i



print "The numbers: "

for b in numbers:
    print b

numbers = []

def printNumbers(max):
    for i in range(0, max):
        print "at the top i is %d" % i
        numbers.append(i)
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    return


max = int(raw_input('Enter an integer > 0: >>'))
print "now we'll use that number"

printNumbers( max )
    
