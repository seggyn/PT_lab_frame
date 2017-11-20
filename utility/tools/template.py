class template:
    def __init__(self, out_path):
        self.out = out_path
        self.path = self.path(out_path)
        self.tpl = open(self.path).read()
    def insert(self, data):
        data = self.string(data)
        output = self.tpl.format(**data)
        open(self.out, 'w').write(output)
    # INNER FUNCTIONS
    def path(self, path):
        a = path.split('.')
        gl = lambda x: '.'.join(x)
        ext, add = a[-1], '.temp.'
        b = gl(a[:-1]).split('\\')
        return 'assets\\' + b[-1] + add + ext
    def string(self, dictionary):
        for key, value in dictionary.items():
            dictionary[key] = str(value)
        return dictionary