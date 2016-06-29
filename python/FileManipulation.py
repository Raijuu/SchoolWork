#!/usr/bin/python

# Open the file for writing
f = open("test.txt","w")
f.write("Hello world\n")
f.close()

# Open the file for appending
f = open("test.txt","a")
f.write("This is the end\n")
f.close()

# Open the file for reading and modification
f = open("test.txt","r+")

# Print file contents
print "Current contents are:\n" + f.read()

# Go to the end of the file and append
f.seek(0,2)

print "Starting file length is %d" % f.tell()

f.write("This is the new end!\n")

print "End file length is %d" % f.tell()

# Go back to the beginning of the file for reading
f.seek(0,0)
print "\nNew contents are:\n" + f.read()

f.close()
