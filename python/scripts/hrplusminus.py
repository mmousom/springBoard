import sys
while True:
    """a = raw_input("How many numbers : \n")
    l = raw_input("All numbers : \n")"""
    a = raw_input()
    l = raw_input()
    if len((l.split(" "))) != int(a) :
        print "you haven't entered all numbers, try again..."
        continue
    else:
        break
l = l.split(" ")
ln = len(l)
plus = [value for value in l if int(value) > 0]
minus = [value for value in l if int(value) < 0]
zeros = [value for value in l if int(value) == 0]

print len(plus)/float(ln)
print len(minus)/float(ln)
print len(zeros)/float(ln)
