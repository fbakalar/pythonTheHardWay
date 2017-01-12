#---------------------------------------------------------|
#
#  Exercise 38  Doing things to Lists
#   
#  a "data Structure" is just a formal way to structure or 
#   organize some data (facts)
#   
#  just a way to store facts (data) in a program in an 
#   an organized way so that you can access them in 
#   different ways
#
#  lists are one of the most common data structures 
#  They are ordered lists of facts (data)
#
#  They can be accessed randomly or in order via an index
#  
#  When to use lists:
#  ------------------
# 
#  -main tain an order  -  this is NOT sorted order
#   list DO NOT sort for you
#  -when you need to access contents randomly by a number
#   remember this is CARDINAL (eg start at 0)
#  -if you need to go through contents linearly (first to last)
#   remeber that is what a <for loop> does
#
#
#  Study:
#  -------
#
#  more_stuff.pop()  
#    reads as 'Call <pop> on more_stuff'
#  pop(more_stuff) does the SAME thing
#
#  review basics of Object Oriented
#  review a python 'Class' (not the same as other languages)
#
#
#---------------------------------------------------------|


        
    
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list.  Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)


print "there we go: ", stuff

print stuff[1]
print stuff[-1] # whoa! fancy - prints last item in list
print stuff.pop() # pops and again prints last item 
print ' '.join(stuff) # what? cool! no brackets and sana last item
print '#'.join(stuff[3:5]) # super stellar!

# [3:5]  is similar to range (3,5)
#  extract item 3 to item 4 -  exclude item 5





