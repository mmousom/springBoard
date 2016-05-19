d = {}
n = int(raw_input())
for i in range(n):
    x = raw_input().split(" ")
    d[x[0]] = float(float(x[1]) + float(x[2]) + float(x[3])) / 3
name = raw_input()
print '{0:.2f}'.format(d[name])    