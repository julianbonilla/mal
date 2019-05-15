import re


class Reader:
    def __init__(self, tokens, position=0):
        self.tokens = tokens
        self.position = position

    def next(self):
        self.position += 1
        return self.tokens[position-1]

    def peak(self):
        if len(self.tokens) > self.position:
            return self.tokens[self.position]
        else:
            return None

def read_str(str):
    tokens = tokenize(str)
    return read_form(Reader(tokens))

def tokenize(str):
    tre = re.compile(r"""[\s,]*(~@|[\[\]{}()'`~^@]|"(?:\\.|[^\\"])*"?|;.*|[^\s\[\]{}('"`,;)]*)""")
    return [t for t in re.findall(tre, str) if t[0] != ';']

def read_form(reader):
    pass
