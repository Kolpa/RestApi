import time


class Todo:
    def __init__(self, tid, name, description):
        self.tid = tid
        self.name = name
        self.description = description
        self.time = time.time()