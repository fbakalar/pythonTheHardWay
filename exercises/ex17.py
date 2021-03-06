############################################################################
#
#   This is exercise 17 from 'Python The Hard Way'
#
#    File Operations
#    This script will copy one file to another file
#
#############################################################################


from sys import argv
from os.path import exists  #This returns True if a file exists

# assert isinstance(argv, object)   #added by pycharm
scripts, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)


# we could do these two on one line, how?

in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)   #use of the exists method we imported
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()
