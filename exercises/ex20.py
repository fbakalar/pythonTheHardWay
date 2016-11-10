#####################################################
#
#   Exercise 20 from Python The Hard Way
#
#    Functions and Files
#   C:\Users\berni\Documents\Source\pythonTheHardWay\exercises
#
#   just making some changes to test on MAC
#
#####################################################

from sys import argv

script, input_file = argv

# this defines the function print_all
def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)  # this calls print_all

print "Now let's rewind, kind of like a tape."

rewind(current_file)  # set current_file back to the start of file

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
