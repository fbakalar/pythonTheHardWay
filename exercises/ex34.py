#---------------------------------------------------------|
#
#  Exercise 34 Accessing Elements of Lists
#   
#  
#  Python starts its lists at 0 rather than 1
#  
#  It seems weird, but there are many advantages to this
#
#  the difference boils down to the difference between
#
#  'ordinal'  and 'cardinal'  numbers
#
#  'Ordinal' lists begin with 1
#  'Cardinal' lists begin with 0
#     an element's ordinal (subscript) equals 
#     the number of elements preceding it in the sequence
#
# cardinal = ordinal -1
#
#---------------------------------------------------------|


animals = ['bear', 'python', 'peacock', 'angaroo', 'whale', 'platypus']

# The animal at 1
print "The animal at position #1 is: ", animals[1]

# The third (3rd) animal
print "The 3rd is: ", animals[2]

# the first (1st) animlmal
print "The 1st is: ", animals[0]

# the animal at 3
print "The animal at position #3 is: ", animals[3]

# the fifth(5th) animal
print "The 5th is: ", animals[4]

# the animal at 2
print "The animal at #2 position is: ", animals[2]

# The sixth(6th) animal
print "The 6th is: ", animals[5]

# the animal at 4
print "The animal at position #4 is: ", animals[4]