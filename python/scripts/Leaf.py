class Leaf(object):
    """ A leaf falling in the woods"""
    def __init__(self, color="green"):
        self.color = color
    def   __str__(self):
        return "A {} color leaf".format(self.color)
        