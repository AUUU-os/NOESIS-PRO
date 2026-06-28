import json
class LegacyCapsule:
    def seal(self, artifacts, path='capsule.json'):
        with open(path,'w') as f:
            json.dump(artifacts,f)
        return 'capsule sealed'
