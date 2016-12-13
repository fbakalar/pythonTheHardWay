#---------------------------------------------------------|
#
#  Exercise 36: Designing and Debugging
#
#
#   Use a while-loop only to loop forever, and that means 
#   probably never. This only applies to Python; 
#   other languages are different.
#
#    Use a for-loop for all other kinds of looping, 
#    especially if there is a fixed or limited number 
#     of things to loop over.
#   
#  
#  
#
#---------------------------------------------------------|

import sys


 # A tuple of strings giving the names of all modules that are 
 #  compiled into this Python interpreter.  
 #  (This information is not available in any other way

'''
print sys.builtin_module_names  

print sys.flags

print sys.float_info

print sys.version

'''

def door_one():
   print 'put some stuff here'

def door_two():
   print 'put some other stuff here'

def trap_door():
    print 'what happens on the trap door'

def window_right():
    print 'window right'

def window_left():
    print 'window left'

def start():
    print 'the start'
    print 'Congratulations!  you get to choose'
    print 'There are 2 doors in front of you'
    print 'Which one do choose?'
    print 'door number 1 or door number 2?'

    choice1 = raw_input('> ')
    
    if '1' in choice1 or 'one' in choice1:
        print 'OK'
        print 'you choose door number 1!'
        print ''
        print "choice1 = 5"
    else:
        print "choice1 != 5"

start()