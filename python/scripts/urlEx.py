from urllib import urlopen

url = "http://learncodethehardway.org/words.txt"
#url = "http://cnn.com"
WORDS = []

for i in urlopen(url).readlines():
    WORDS.append(i.strip().split(" "))

print  'Total word count :%d' %len(WORDS)     
print sorted(WORDS )

