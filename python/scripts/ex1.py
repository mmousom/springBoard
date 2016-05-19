#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.

def ex1():
	l=[]
	for i in range(2000, 3201):
    	   if (i%7==0) and (i%5!=0):
                l.append(i)
#print l
	return ','.join(str(v) for v in l)
#print ','.join(str(l))

"""Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320"""

def fact(n):
        if n == 0:
            return 1
	if n<0:
		print "Invalid Number, factorial can't be computed"
	return n* fact(n-1)


def gendic():
    print "Enter an integer :"
    n=int(raw_input())
    dic=dict()
    for i in range(1,n+1):
        dic[i]=i*i
    return dic

def convert():
    print "Enter numbers separated by comma:"
    l=raw_input()
    v=l.split(",")
    t=tuple(v)
    print v
    print t


class InputOutputString(object):
	def __init__(self):
		self.s="Default"
	def getString(self):
		self.s=raw_input()
	def printString(self):
		print self.s.upper()
	def __repr__(self):
	    return "{} (s='{}')".format(self.__class__.__name__,self.s)
	def __str__(self):
	    return self.__class__.__name__
import math
def q6():
    c=50
    h=30
    value=[]
    d=[x for x in raw_input().split(',')]
    for dd in d:
        value=math.sqrt((2 * c * float(dd)/h))
    return value

def q7():
    inputStr=raw_input()
    dimensions=[int(x) for x in inputStr.split(',')]
    rowNum=dimensions[0]
    colNum=dimensions[1]
    multiList = [[0 for col in range(colNum)] for row in range(rowNum)]
    for r in range(rowNum):
        for c in range(colNum):
            multiList[r][c]=r*c
    return multiList

def q8():
    pinputList=[x for x in raw_input().split(',')]
    pinputList.sort()
    print ','.join(pinputList)

def q9():
    lines=[]
    while True:
        s=raw_input()
        if s:
            lines.append(s.upper())
        else:
             break;
    for x in lines:
       print x

def q10():
    lines=[ x for x in raw_input().split(" ")]
    linesset=" ".join(sorted(set(lines)))
    print linesset

def q11():
    values=[]
    numlist=[x for x in raw_input().split(",")]
    for i in numlist:
        intp = int(i,2)
        if intp%5 == 0:
            values.append(i)
    print ",".join(values)

def q12(lrange=1000,urange=3001):
    values=[]
    xx=[str(i) for i in range(lrange,urange+1,2)]
    for i in xx:
        x=str(i)
        if (int(x[0])%2== 0 and int(x[1])%2==0 and int(x[2])%2==0 and int(x[3])%2==0):
            values.append(x)
    return ','.join(values)

def q13():
    inp=raw_input()
    d={"LETTERS":0,"NUMBERS":0}
    for c in inp:
        if c.isalpha():
            d["LETTERS"]+=1
        elif c.isdigit():
            d["NUMBERS"]+=1
        else:
            pass
    print "LETTERS :",d["LETTERS"]
    print "NUMBERS :",d["NUMBERS"]

def q14():
    inp = raw_input()
    d={"Upper":0,"Lower":0}
    for c in inp:
        if c.islower():
        	d["Lower"]+=1
        elif c.isupper():
        	d["Upper"]+=1
        else:
        	pass
    print d

def q15():
	a=raw_input()
	n1=int("%s" % a)
	n2=int("%s%s" % (a,a))
	n3=int("%s%s%s" %(a,a,a))
	print n1+n2+n3

def q16():
	l=raw_input()
	x=[i for i in l.split(",") if int(i)%2!=0]
	print ",".join(x)

def q17():
        netAmount=0
	while True:
		s=raw_input()
		if not s:
			break
		values=s.split(" ")  # create a list off the string input
		operation=values[0]
		amount=int(values[1])
		if operation == "D":
			netAmount=amount+netAmount
		if operation == "W":
			netAmount=-amount+netAmount
		else:
			pass
	print netAmount

import re
def q18():
	value=[]
	inp=raw_input()
	inpl=inp.split(",")
	for p in inpl:
		if len(p) < 6 or len(p) > 12:
			continue
		else:
			pass
		if not (re.search("[a-z]",p)):
			continue
		elif not (re.search("[0-9]",p)):
			continue
		elif not (re.search("[A-Z]",p)):
			continue
		elif not (re.search("[$#@]",p)):
			continue
		else:
			pass
		value.append(p)
	print ",".join(value)

from operator import itemgetter, attrgetter
def q19():
	l=[]
	while True:
		s=raw_input()
		if not s:
			break
		l.append(tuple(s.split(",")))
	sorted(l,key=itemgetter(0,1,2))

def q20(x,*args):
	total=x
	for i in args:
		total=total+i
	print total

def q21(x,**kwargs):
	""" this is an example of keywords args"""
	total=x
	for arg,value in kwargs.items():
		print "adding ", arg
		total+=int(value)
	print "Total =",total

def foo(*args,**kwargs):
	print args, kwargs

import math
def q22():
	pos=[0,0]
	while True:
		s=raw_input()
		if not s:
			break
		directions=s.split(" ")
		if directions[0]=="UP":
			pos[0]+=int(directions[1])
		if directions[0]=="DOWN":
			pos[0]-=int(directions[1])
		if 	directions[0]=="RIGHT":
			pos[1]+=int(directions[1])
		if 	directions[0]=="LEFT":
			pos[1]-=int(directions[1])
		else:
			pass
	return math.sqrt(pos[0]*pos[0]+pos[1]*pos[1])

def q23():
	dic={}
	while True:
		s=raw_input()
		if not s:
			break
		words=s.split(" ")
		for i in words:
			if i in dic:
				dic[i]+=1
			else:
				dic[i]=1
	k=dic.keys()
	k.sort()
	for w in k:
		print "%s : %d" % (w,dic[w])

class Person:
	# define class parameter nameS
	name="Person"
	def __init__(self, name="none"):
		self.name = name

class ReverseIterator(object):
	def __init__(self,list):
		self.list = list
		self.index=len(list)
	def __iter__(self):
		return self
	def next(self):
		self.index -=2
		if self.index>=0:
			return self.list[self.index]
		else:
			raise StopeIteration()

def summation(x):
	sum=0
	if type(x)!=int:
		return  "Error 404"
	for i in range(1,x+1):
		sum+=i
	return sum

def sumsmart(x):
	return x*(x+1)/2 if isinstance(x,int) else "Error 404"

def friend(x):
	myfriend=[]
	for i in x:
		if len(i) == 4:
			myfriend.append(i)
	return myfriend

def smartfriend(x):
	return [f for f in x if len(f)==4]

class Block:
	def __init__(self,list):
		self.width=list[0]
		self.length=list[1]
		self.height=list[2]

	def get_width(self):
		return self.width
	def get_height(self):
		return self.height
	def get_length(self):
		return self.length
	def get_volume(self):
		return self.width*self.length*self.height
	def get_surface_area(self):
		return 2*(self.width*self.length+self.length*self.height+self.height*self.width)

def trigrams(phrase):
	phrase=phrase.replace(" ","_")
	return " ".join([phrase[i:i+3] for i in range(len(phrase)-2)])

def identify_weapon(character):
	weapon={'Cragger':'Vengdualize',
			'Mousom':'Sarcasm',
			'Annika':'Humility',
			'Lopita':'Compassion'}
	print weapon.get(character,'Not a valid character')
	try:
		print weapon[character]
	except:
		print 'Not a valid character'
def count(array):
	d={}
	for i in array:
		if d.has_key(i):
			d[i]+=1
		else:
			d[i]=1
	return d

from collections import Counter


def cnt_1(array):
	return Counter(array)


def cnt_2(array):
	ed = {}
	for i in array:
		ed[i] = ed.get(i, 0)+1
	return ed
	
def findFactors(x):
    ll = ()
    for i in range(1,int(math.sqrt(x))+1):
        if x%i == 0:
           ll.append(i,x/i) 
    return set(ll)
    	
