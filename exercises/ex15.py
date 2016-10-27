###############################################
#
#  Python The Hard Way
#         ex 15.py
#
#################################################

from sys import argv

sript, filename = argv

txt = open(filename)

print "here is your file %r: " % filename
print txt.read()

print "type the filename again:"
file_again = raw_input(">>")

txt_again = open(file_again)

print txt_again.read()


