class ArchitectureValidator:
    REQUIRED = ['core','memory','agents','worlds']

    def validate(self, tree):
        return all(x in tree for x in self.REQUIRED)
