class HomeWorldMode:
    def __init__(self):
        self.state = 'safe'

    def enter(self):
        return 'Home world entered.'
