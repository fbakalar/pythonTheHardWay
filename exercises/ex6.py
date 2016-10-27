# this line sets X = to a string that uses a placeholder character
# that is substituted with the number 10
x = "There are %d types of people." % 10

# set the binary variable value = to the string 'binary'
binary = "binary"

# set do_not variable = to string 'don't'
do_not = "don't"

# this line sets Y = to a string that uses placeholder charcters
# that are substituted with strings that are held by
# the variables previously defines as binary and do_not
y = "Those who know %s and those who %s." % (binary, do_not)


# this line prints the variable X.  The next prints Y
print x
print y

print()

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation # %hilarious

w = "This is the left side of..."
e = "a string with a right side."

# the following line uses the print command to concatenate 
# 2 strings
print w + e

