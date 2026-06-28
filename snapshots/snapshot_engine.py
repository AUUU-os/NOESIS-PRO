import json, time

class SnapshotEngine:
    def save(self, state):
        fn = f'snapshot_{int(time.time())}.json'
        with open(fn,'w') as f:
            json.dump(state,f)
        return fn
