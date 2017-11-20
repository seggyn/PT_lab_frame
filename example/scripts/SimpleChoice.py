from scripts.Choice import *

class SimpleChoice(Choice):
    def __init__(self, array, n = 0):
        self.data, self.n = array, n
        if n <= 0:
            raise NameError('n isn`t positive number.')
        # INTERACTION WITH ENTITY OBJECT
        self.arguments['Choice'] = [ self.n ]
        self.fast_get()
    @add2queue(0, 'choice')
    def Choice(self, n):
        try:
            result = np.random.choice(self.data, n, replace=False)
        except:
            result = np.random.choice(self.data, n, replace=True)
        self.n, self.lenSet = n, len(result)
        return result
    @add2queue(1, 'table')
    def Table(self):
        self.array = np.unique(self.choice, return_counts=True)
        self.setX, self.setN = self.array
        self.set = np.stack(self.array, axis=-1)
        table = pd.DataFrame({'X': self.setX, 'N': self.setN})
        return table.set_index('N').transpose()
    @add2queue(6, 'mode')
    def Mode(self):
        i = np.where(self.setN == np.max(self.setN))
        return self.setX[i]
    @add2queue(7, 'median')
    def Median(self):
        i = round(len(self.setX) / 2)
        if len(self.setX) % 2 == 1:
            result = self.setX[i]
        else:
            result = (self.setX[i-1] + self.setX[i]) / 2
        return result