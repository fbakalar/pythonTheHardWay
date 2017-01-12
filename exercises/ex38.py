#---------------------------------------------------------|
#
#  Exercise 38  Doing things to Lists
#   
#  
#
#   
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