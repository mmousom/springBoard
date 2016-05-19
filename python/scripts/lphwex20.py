from sys import argv

argv = ["lphwex15.py","lphwex15_sample.txt"]
script, input_file = argv

def print_all(f):
    print f.read()
    
def rewind(f):
    f.seek(0)
    
def print_a_line(lineno,f):
    print lineno, f.readline()            

# First lets open the file
ff = open(input_file)
#lets printout the whole file
print ff.read()

print "Lets rewind and go back to begining of the file"

rewind(ff)
ln=1

print "Lets read one line at a time"

print_a_line(ln, ff)
ln+=1
print_a_line(ln, ff)
ln+=1
print_a_line(ln, ff)

ff.close()
