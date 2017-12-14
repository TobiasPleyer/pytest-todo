import re


class TodoChecker(object):
    todo_re = re.compile(r'([#: ]+todo[#: ]*)|(^todo\W+)', re.IGNORECASE)
    def __init__(self, options, path):
        self.path = path
        self.hasErrors = False
        self.found = []

    def check(self):
        with open(self.path, 'r') as fp:
            for lnum, text in enumerate(fp):
                m = self.todo_re.search(text)
                if m:
                    self.found.append({'lnum': lnum, 'text': text})
        if self.found:
            self.hasErrors = True

    def summary(self):
        summary = "File {}\n".format(self.path)
        summary += "Found {} TODOs\n\n".format(len(self.found))
        info = "    Line {lnum}: {text}"
        summary += '\n'.join([info.format(**todo) for todo in self.found])
        return summary