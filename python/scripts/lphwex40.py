class Song(object):
    """ This is a simple class , with methid and and constructor"""
    def __init__(self,l):
        self.lyrics = l
        
    def sing_me_song(self):
        print self.lyrics    

class FolkSong  (Song):
    def __init__(self,origCntry):
        self.origin =  origCntry
                     
        
hbd = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])
                   
bop = Song(["They rally around tha family",
                        "With pockets full of shells"])
                                           
hbd.sing_me_song()
bop.sing_me_song()
                                                      