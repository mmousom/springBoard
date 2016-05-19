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
s=0
for x in l:
    s = s + int(x)
print (s)
