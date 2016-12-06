#---------------------------------------------|
#
#  Exercise 31:  Making Decision
#
#
#
#---------------------------------------------|


print "You enter a dark room with three doors.  Do you go through door #1 or door #2?"
print "or the mystery door...#3?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake.  What do you do?"
    print "1. Take the cake."
    print "2.  Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
	    print "The bear eats your face off.  Good job!"
    elif bear == "2":
	    print "The bear eats your legs off.  Good job!"
    else:
	    print "Well, doing %s is probably better.  Bear runs away."  % bear

elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."

	insanity = raw_input("> ")

	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello.  God job!"
	else:
		print "The insanity rots your eyes into a pool of muck.  Good job!"

elif door =="3":
    print "you've entered another demension. There are two open windows"
    print "What do you do?"
    print "L. climb through the left window"
    print "R. climb through the right window"
    print "C. leave the room and close the door"
   
    window = raw_input("> ")
   
    if window == "L" or window == "R":
    	print " Now you are standing in a field of grass.  Good job!"
    	print "there is a path that forks"
    	print "to the left is a sign that reads 'easy'"
    	print "to the right a sign that reads 'hard'"
    	print "which way do you go"
    	print "E. easy"
    	print "H. hard"

    	fork = raw_input("> ")

    	if fork == "E":
            print "Easy way eh?"
            print "ok then - be that way..."
        elif fork == "H":
            print "Congratulations you are in for a world of pain and struggle"
            print "but"
            print "in the end - if you stay the course it will all be worth it"
        else:
            print "you are transported back to insanity"
    else:
        print "DUDE"
        print "seriously?"
        print " oh .......well....."

else:
    print "BOOM!!!!!"
    print "You stumble around and fall on a knofe and die.  Good job!"


