from sys import maxsize


class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return f"{self.id}:{self.name}"

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
                and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def fill_if_none(self, other):
        if self.name is None:
            self.name = other.name
        if self.header is None:
            self.header = other.header
        if self.footer is None:
            self.footer = other.footer
        if self.id is None:
            self.id = other.id