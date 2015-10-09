class Leaf(object):
    def __init__(self,color="green"):
        self.color="green"
    def fall(self):
        print "splat!"
        
class MapleLeaf(Leaf):
    def changeColor(self):
        self.color="red"
    def fall(self):
        self.changeColor()
        print "splunk!"                    