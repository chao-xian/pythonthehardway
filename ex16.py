# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

print "We're going to erase %r" % filename
print "If you don't want that, hit Ctrl+C (^C)"
print "If you do want that, hit RETURN (⏎)"

raw_input('?')

print "Opening th file..."
target = open(filename, 'r+')

print "The current contents of the file %r is..." % filename
print target.read()

print "Truncating the file. Bye!"
target.truncate(0)

print "Now I'm going to ask you for three lines"

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file"

lines = "{0}\n{1}\n{2}".format(line1, line2, line3)
target.write(lines)

print "New contents are...\n"
target.seek(0)
print target.read()

print "And finally, we close it"
target.close()
