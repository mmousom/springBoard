from sys import argv

argv = ["lphwex15.py","lphwex15_sample.txt"]
script, filename = argv

print "we are going to erase file : %s" % (filename)
print "If you don't want that hit ctrl-C ( ^C)."
print "If you want that hit, RETUN"

raw_input("?")

print "Opening the file %r" %(filename)
target = open(filename,"w")

print "Truncating the file  :%r" %(filename)
target.truncate()

print "Enter 3 lines"
line1 = raw_input("Line 1 :")
line2 = raw_input("Line 2 :")
line3 = raw_input("Line 3 :")

print "Writing those 3 lines to the file"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print "Closing file : %r" %(filename)

target.close()        