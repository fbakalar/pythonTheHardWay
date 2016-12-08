#---------------------------------------------------------------------|
#
#   Exercise 32:  Loops & Lists
#
#
#  Lists are exactly what their name says: 
#   a container of things that are organized in order from 
#   first to last
#
#----------------------------------------------------------------------|

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a List
for number in the_count:
	print "This is count %d" % number

# same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit

# also we can go through mized lists too
# notice we have to use %r since we don't know what's in it
for i in change:
	print "I got %r" % i

# we can also build lists, first start with an empty one 
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
	print "Adding %d to the list." % i
	# append is a function that lists undestand
	elements.append(i)

# now we can print them out too
for i in elements:
	print "Element was: %d" % i

elements = []
elements = range(7 ,13)   #assinged a range to elements

print "Now using range"
print "Element was: %s" % elements[0]  #print first value in range