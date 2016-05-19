a = raw_input()
for i in range(1,int(a)+1):
    print "%*s" % (int(a)-i-1,'#' * i)
