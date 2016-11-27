#--------------------------------------------------------|
#
#  exercise 27
#  this is all about Boolean Algebra
#
# It is thus a formalism for describing 
# logical relations in the same way that ordinary 
#  algebra describes numeric relations.
# http://www.math.uwaterloo.ca/~snburris/htdocs/MYWORKS/PREPRINTS/aboole.pdf 
# http://www.gutenberg.org/files/15114/15114-pdf.pdf?session_id=143943e9be8ee78786193d94757956efda614713
#--------------------------------------------------------|

"""
NOT	         True?
------------|------
not False	| True
not True	| False

OR	              True?
----------------|-------
True or False	| True
True or True	| True
False or True	| True
False or False	| False

AND	               True?
-----------------|-------
True and False	 | False
True and True	 | True
False and True	 | False
False and False	 | False

NOT OR	                True?
----------------------|------
not (True or False)	  | False
not (True or True)	  | False
not (False or True)	  | False
not (False or False)  |	True

NOT AND	                True?
-----------------------|-----
not (True and False)   | True
not (True and True)	   | False
not (False and True)   | True
not (False and False)  | True

!=	True?
1 != 0	True
1 != 1	False
0 != 1	True
0 != 0	False

==	True?
1 == 0	False
1 == 1	True
0 == 1	False
0 == 0	True
"""