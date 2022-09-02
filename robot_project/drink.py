class Drink:
    def __init__(self, name, idnum):
        self.name = name
        self.id = idnum
        self.filled = True

    def set_empty(self):
        self.filled = False

    def is_empty(self):
        return not self.filled
