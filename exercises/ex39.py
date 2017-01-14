#---------------------------------------------------------|
#
#  Exercise 39  Dictionaries
#   
#  a dictionary is an alternative way to store data in python
#  similar to a list - but - instead of using numbers 
#   to access the data you can use almost anything
#
#  so a <dict> becomes almost like a database for storing  
#   and organizing data
#   
#  looks like a <dict> is a key value pair...
#
#
#
#---------------------------------------------------------|


# create a mapping of state to abbreviation

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}        

# create a basic set of states and some cities in them

cities = {
    'CA': 'San Francisco',
    'MI': ['Detroit'],  # in order to add values to one key
    # you need to set the key = to a list rather than a string
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print some cities
print '-' * 20
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]
    
# add another city for Michigan
#cities['MI'] = 'Saginaw'  # replaces Detroit
cities['MI'].append('Saginaw')  # add Saginaw

print '-' * 20
print 'updated Michigan'
print "Michigan has: ", cities[states['Michigan']]


# print some states
print '-' * 20
print "Mighigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict
print '-' * 20
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
# note variable names 'state' and 'abbrev' are 
# arbitrary labels.  I could also use a & b
print '-' * 20
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '-' * 20
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)


# now do both at the same time
print '-'* 20
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])

print '-' * 20
#














