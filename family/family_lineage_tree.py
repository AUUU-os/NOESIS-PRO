class FamilyLineageTree:
    def __init__(self):
        self.members = {}

    def add(self, name, parent=None):
        self.members[name] = parent
