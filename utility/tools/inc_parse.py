from utility.includes import *

class inc_parse:
    class data:
        class path:
            pass
    def __init__(self):
        i, o = ['input', 'output']
        condition, ext = 'extension' not in globals(), extension
        self.extension = ext = '' if condition else '.' + ext
        f = lambda x: globals()[x] + ext
        p, d = self.data.path, self.data
        if i in globals():
            setattr(p, i, f(i))
            setattr(d, i, self.get(f(i)))
        if o in globals():
            setattr(p, o, f(o))
    @classmethod
    def get(cls, path):
    # @ path = (short) full path with ext
        f = open(path)
        lines = f.readlines()
        f.close()
        return [int(l) for l in lines]