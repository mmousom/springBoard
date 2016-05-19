def getnextbigger(s):
    length = len(s)
    for i in range(length-1,0,-1):
        if ord(s[i]) > ord(s[i-1]):
            sw = s[i-1]
            s[i-1] = s[i]
            s[i] = sw
            return s
        return s

a = raw_input()
i=1
inp = []
while i <= a:
    ss = raw_input()
    s = getnextbigger(ss)
    if s == ss:
        print 'No Answer'
    else:
        print s
    # get next lexicographical bigger word
    i=i+1
