class entity:
    arguments = {}
    # QUEUE VARS
    is_queue_form = False
    method_set, queue_set = [], {}
    def fast_get(self):
        for method_name in dir(self):
            if callable(getattr(self, method_name)):
                if method_name[0] != '_':
                    if getattr(self, method_name).__name__ == 'wrapper':
                        self.method_set.append(method_name)
        for method in self.method_set:
            self.start_function(method)
        temp = sorted(self.queue_set.items(), key=lambda x: x[1])
        _queue = [key for key, value in temp]
        self.is_queue_form = True
        for method in _queue:
            self.start_function(method)
    def start_function(self, name):
        f = getattr(self, name)
        try:
            if name in self.arguments:
                f(*self.arguments[name])
            else: f()
        except AttributeError: pass
    @classmethod
    def toFunName(cls,s):
        return s[0].upper() + s[1:]
    @classmethod
    def toVarName(cls,s):
        return s[0].lower() + s[1:]

# @ name - (sense) variable name
def add2queue(num, name):
    def real_decorator(fn):
        def wrapper(self, *args, **kwargs):
            fun_name = fn.__name__
            if not self.is_queue_form:
                self.queue_set[fun_name] = num
            else:
                if fun_name in self.arguments:
                    args = self.arguments[fun_name]
                value = fn(self, *args, **kwargs)
                setattr(self, name, value)
        return wrapper
    return real_decorator


