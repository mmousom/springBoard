from sys import argv
from os.path import exists

argv = ["lphwex17.py","lphwex15_sample.txt","target.txt"]
script, source, target =  argv

print "This program will copy from %r to %r" %(source,target)

#Read input file

infile = open(source)
indata = infile.read()

print "Outfile exists : %r" %(exists(target))
outfile = open(target,'w')
print "Writing data of %r byte" %(len(indata))
outfile.write(indata)

print "Closing files"
infile.close()
outfile.close()


