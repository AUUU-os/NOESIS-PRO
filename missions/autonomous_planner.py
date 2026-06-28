class AutonomousMissionPlanner:
    def __init__(self):
        self.queue=[]
    def derive(self, context):
        mission={'goal':f'Optimize {context}','priority':'high'}
        self.queue.append(mission)
        return mission
