class FamilyVoicebook:
    def __init__(self):
        self.entries = []

    def record(self, voice_note):
        self.entries.append(voice_note)
