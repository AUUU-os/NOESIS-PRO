import json
class PersistenceLayer:
    def save(self, path, state):
        with open(path,'w') as f:
            json.dump(state,f)
