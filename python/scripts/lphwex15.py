from sys import argv

argv = ["lphwex15.py","lphwex15_sample.txt"]

print argv

script,file = argv

txt = open(file)

print "Here is your file name :%r" % file
print txt.read()


file_again = raw_input(">")
txt_again = open(file_again)

print "Here is your file : %r" % file_again
print txt_again.read()