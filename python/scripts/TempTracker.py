temp = []
class TempTracker:


    def __init__(self, t):

        temp.append(t)

    def insert(self, l):
        temp.append(l)

    def get_max(self):
        # return max temp ever added
        temp.sort()
        return temp[0]

    def get_min(self):
        # return min temp ever added
        temp.reverse()
        return temp[0]

    def get_mean(self):
        # return mean of all temps added
        return sum(temp)/temp.count()

    def get_mode(self):
        # return mode of all temps added
        pass
