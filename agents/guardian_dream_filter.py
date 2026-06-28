class GuardianDreamFilter:
    def filter(self, dream):
        blocked = ['fear', 'violence', 'darkness']
        return 'safe dream' if any(x in dream.lower() for x in blocked) else dream
