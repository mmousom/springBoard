#import __future__
#n = int(raw_input())
#l =[]
#for i in range(1,n+1):
#    l.append(i)
#print ''.join(map(str,l))   

# in one line 

print ''.join(map(str,[i for i in range(1,int(raw_input()))]))

