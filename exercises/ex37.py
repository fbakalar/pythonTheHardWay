#----------------------------------------------------------|
#
#   Exercise 37:  Symbol Review - KEYWORDS
#
#   https://learnpythonthehardway.org/book/ex37.html
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
    Python’s for statement iterates over 
        the items of any sequence (a list or a string), 
        in the order that they appear in the sequence

in:

yield:

pass:
   Does nothing
   can be used as a placeholder when working on code

range:
    iterartes over a sequence of numbers.
    Generates lists containing arithmentic progressions
    To iterate over the indices of a sequence, 
        you can combine range() and len() 
        for i in range(len(a)):
    Can specify a start, end, step
        range(0, 10, 3)  goes from 0 to 10 by 3
          [0, 3, 6, 9]


xrange:

'''

# ERROR and EXCEPTIONs
'''
There are 2 types of errors
    Syntax errors
        Also known as 'parsing errors'
        The parser repeats the offending line and 
            displays a little ‘arrow’ pointing at the earliest 
            point in the line where the error was detected.


    Exceptions
        Errors detected during execution are called exceptions 
            and are not unconditionally fatal:
        These errors can be handled within the code
        Most exceptions are not handled by programs, however, 
           and result in error messages
           ex:
               >>> 10 * (1/0)
                Traceback (most recent call last):
                  File "<stdin>", line 1, in <module>
                ZeroDivisionError: division by zero
               >>> 4 + spam*3
                Traceback (most recent call last):
                  File "<stdin>", line 1, in <module>
                NameError: name 'spam' is not defined

Use TRY  EXCEPT to handle exceptions
    try:
      First, the try clause is sexecuted
      If no exception occurs, the except clause is skipped
         execution of the try statement is finished.
      If an exception occurs during execution of the try clause, 
         the rest of the clause is skipped
         if its type matches the exception named after the except keyword
            the except clause is executed, and 
            then execution continues after the try statement.
    except <exception>:
      A try statement may have more than one except clause
          to specify handlers for different exceptions
      An except clause may name multiple exceptions 
          as a parenthesized tuple
          ex:
          except (RuntimeError, TypeError, NameError):

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
    allows the programmer to force a specified exception to occur
'''

# FUNCTIONS and CLASSES
'''
def:
class:
return:
lambda:
'''






