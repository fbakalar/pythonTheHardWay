#----------------------------------------------------------|
#
#   Exercise 37:  Symbol Review
#
#
#   http://zetcode.com/lang/python/keywords/
#    http://sandbox.mc.edu/~bennet/python/code/
#
#----------------------------------------------------------|


'''
import:
from:
global:
del:

'''


# LOGIC
'''
and: 
    the <and> keyword is used if all conditions in a 
     boolean expression must be met
     ex:
         if age < 55 and sex == 'M':...

not:
    the <not> keyword negates a boolean value
     test a boolean condition
     ex:
        if grade not in grades:...

or:
    the <or> keyword is used if at least one condition 
     must be met

is:  
    tests for object identity / are they identical?
        eg - whether we are talking about the same object
        note: multiple variables may refer to same object
            [] is [] ?  False  - because they are 2 distinct objects
            
    == operator tests for equality
            [] == [] ?  True - because they are equivalent
               even though they are not the same object


assert:
    helps find bugs more quickly and with less pain
    

with - as:
    the with statement simplifies exception handling by 
       encapsulating common preparation and cleanup tasks in 
       so-called context managers.
    Useful when you have two related operations which you’d 
       like to execute as a pair, with a block of code in between
    The classic example is opening a file, manipulating the file, 
       then closing it:
    The advantage of using a with statement is that it is 
       guaranteed to close the file no matter how the nested block 
       exits.
       http://preshing.com/20110920/the-python-with-statement-by-example/
'''

#  IF statements and LOOPS
'''
break:
breaks out of the smallest enclosing for or while loop
continue:
The continue statement, also borrowed from C, 
continues with the next iteration of the loop
if:
elif:
    An if ... elif ... elif ... sequence is a substitute for the 
        switch or case statements found in other languages.
else:
    Loop statements may have an else clause
    executed when the loop terminates through 
    exhaustion of the list (with for) or 
    when the condition becomes false (with while)
    but not when the loop is terminated by a break statement
for:
in:
yield:
pass
'''

# ERROR and EXCEPTIONs
'''
try:
except:

finally:
    set things up
    try:
        do something
    finally:
        tear things down

The try-finally construct guarantees that the “tear things down” 
part is always executed, even if the code that does the work doesn’t 
finish.


raise:
'''

# FUNCTIONS and CLASSES
'''
def:
class:
return:
lambda:
'''






