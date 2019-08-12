import re


class Rex:
    def __init__(self, pattern, repl, count=0, flags=0):
        self.pattern = pattern
        self.repl = repl
        self.count = count
        self.flags = flags

    def converter(self, data):
        resdata = str(data[0])
        resdata = (re.sub(self.pattern, self.repl, resdata, self.count).strip())
        return resdata

    