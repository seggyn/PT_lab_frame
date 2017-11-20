import math, numpy as np, pandas as pd
from utility.tools.entity import entity, add2queue

class Choice(entity):
    @add2queue(3, 'avarage')
    def Avarage(self):
        set, l = self.set, len(self.set)
        return np.sum([x*n for x, n in set])/l
    @add2queue(4, 'dispersion')
    def Dispersion(self):
        set, a = self.set, self.avarage
        array = [math.pow(x - a, 2) * n for x, n in set]
        return np.sum(array)/len(set)
    @add2queue(5, 'standardDeviation')
    def StandardDeviation(self):
        return math.pow(self.dispersion, 1/2)
